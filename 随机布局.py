import random
from mathutils import Vector
import bpy

ele_obj = ['product', 'product.001', 'product.002']
floor_obj = ['物件37', '物件28']

max_iterations = 1000  # 最大循环
loop_iterations = 0  # 当前循环
# 限制定位立方体 各个轴最大大小
x_limit = 6
y_limit = 6
z_limit = 6
random_count = len(ele_obj)  # 定位立方体数量
floor = bpy.data.objects['floor']  # 地板
floor_location = floor.location  # 地板位置
floor_dimensions = floor.dimensions  # 地板尺寸
# 地板4个顶点 中心点在中心
floor_vertices = [floor.matrix_world @ i.co for i in floor.data.vertices]
direction = 'z'  # 在地板得哪个面放置物体
random_x_l_range = [floor_vertices[0][0], floor_vertices[1][0]]  # x轴取值
random_y_l_range = [floor_vertices[0][1], floor_vertices[2][1]]  # y轴取值

all_locations = []  # 所有定位块
all_obj = []


def get_pd_box(obj, pd_box_list):
    """获取cube或者组合对象得边框包围"""
    if obj.type == 'MESH':
        pd_box_list.extend([obj.matrix_world @ Vector(pdBvert) for pdBvert in obj.bound_box])
    for i in obj.children:
        pd_box_list = get_pd_box(i, pd_box_list)
    return pd_box_list


def get_box_list(pd):
    pd_box_list = []
    get_pd_box(pd, pd_box_list)
    max_x = max([v[0] for v in pd_box_list])
    min_x = min([v[0] for v in pd_box_list])
    max_y = max([v[1] for v in pd_box_list])
    min_y = min([v[1] for v in pd_box_list])
    max_z = max([v[2] for v in pd_box_list])
    min_z = min([v[2] for v in pd_box_list])
    pd_box = []
    pd_box.append(Vector((min_x, min_y, min_z)))
    pd_box.append(Vector((min_x, min_y, max_z)))
    pd_box.append(Vector((min_x, max_y, max_z)))
    pd_box.append(Vector((min_x, max_y, min_z)))
    pd_box.append(Vector((max_x, min_y, min_z)))
    pd_box.append(Vector((max_x, min_y, max_z)))
    pd_box.append(Vector((max_x, max_y, max_z)))
    pd_box.append(Vector((max_x, max_y, min_z)))
    # 产品尺寸
    pd_d_x = abs(pd_box[0][0] - pd_box[4][0])
    pd_d_y = abs(pd_box[0][1] - pd_box[2][1])
    pd_d_z = abs(pd_box[0][2] - pd_box[1][2])
    dimensions = [pd_d_x, pd_d_y, pd_d_z]
    return pd_box, dimensions


for i in ele_obj:
    try:
        pd = bpy.data.objects[i]
    except:
        continue
    pd_box, dimensions = get_box_list(pd)
    all_obj.append({'name': pd, 'pd_box': pd_box, 'dimensions': dimensions})


def overlap_interval(check_list):
    """校验区间重叠"""
    # 排序
    a_list = sorted(check_list, key=lambda l: l[0])
    for i in range(0, len(a_list) - 1):
        if a_list[i + 1][0] <= a_list[i][1]:
            return True
    return False


def is_intersect(all_locations, dimensions, location):
    located_flag = False
    obj_flag = False
    for i in all_locations:
        obj = bpy.data.objects[i]
        obj_x_range = [obj.location.x - obj.dimensions.x, obj.location.x + obj.dimensions.x]
        o_x_range = [location[0] - dimensions[0], location[0] + dimensions[0]]
        check_x = overlap_interval([obj_x_range, o_x_range])
        obj_y_range = [obj.location.y - obj.dimensions.y, obj.location.y + obj.dimensions.y]
        o_y_range = [location[1] - dimensions[1], location[1] + dimensions[1]]
        check_y = overlap_interval([obj_y_range, o_y_range])
        # obj_z_range = [obj.location.z - obj.dimensions.z, obj.location.z + obj.dimensions.z]
        # o_z_range = [location[2] - dimensions[2], location[2] + dimensions[2]]
        # check_z = overlap_interval([obj_z_range, o_z_range])
        if check_x or check_y:
            located_flag = True
            break
    for i in floor_obj:
        try:
            pd = bpy.data.objects[i]
        except:
            continue
        pd_box, dimensions = get_box_list(pd)
        obj_x_range = [pd_box[0][0], pd_box[4][0]]
        o_x_range = [location[0] - dimensions[0], location[0] + dimensions[0]]
        check_x = overlap_interval([obj_x_range, o_x_range])
        obj_y_range = [pd_box[0][1], pd_box[2][1]]
        o_y_range = [location[1] - dimensions[1], location[1] + dimensions[1]]
        check_y = overlap_interval([obj_y_range, o_y_range])
        if check_x or check_y:
            obj_flag = True
            break
    return located_flag or obj_flag


def generate_located(all_locations):
    global loop_iterations
    # while len(all_locations) < random_count:
    while len(all_locations) < random_count and loop_iterations < max_iterations:
        data = all_obj[0]
        pd = data['name']
        obj_dimensions = data['dimensions']
        loop_iterations += 1
        dimensions_x = round(random.uniform(obj_dimensions[0], obj_dimensions[0] + 0.5), 4)  # 随机 立方体 x 尺寸
        dimensions_y = round(random.uniform(obj_dimensions[1], obj_dimensions[1] + 0.5), 4)  # 随机 立方体 y 尺寸
        dimensions_z = round(random.uniform(obj_dimensions[2], obj_dimensions[2] + 0.5), 4)  # 随机 立方体 z 尺寸
        location_x = round(
            random.uniform(random_x_l_range[0] + dimensions_x / 2, random_x_l_range[1] - dimensions_x / 2),
            4)
        location_y = round(
            random.uniform(random_y_l_range[0] + dimensions_y / 2, random_y_l_range[1] - dimensions_y / 2),
            4)
        location_z = dimensions_z / 2 + floor_location[2]
        dimensions = [dimensions_x, dimensions_y, dimensions_z]
        location = [location_x, location_y, location_z]
        flag = is_intersect(all_locations, dimensions, location)
        if not flag:
            name = 'located_{}'.format(len(all_locations))
            try:
                lp = bpy.data.objects[name]
                lp.location = location
                lp.dimensions = dimensions
                bpy.context.view_layer.update()
            except:
                bpy.ops.mesh.primitive_cube_add(location=location, scale=(1, 1, 1))
                lp = bpy.context.object
                lp.name = name
                lp.display_type = 'BOUNDS'
                lp.dimensions = dimensions
            all_locations.append(name)
            lp_box = [lp.matrix_world @ Vector(lpBvert) for lpBvert in lp.bound_box]  # pd 外边框 8个顶点得xyz全局坐标系
            # 这儿会牵扯到 原点位置信息 导致计算位移不准确
            pd.location.x = (lp_box[0][0] + lp_box[4][0]) / 2
            pd.location.y = (lp_box[0][1] + lp_box[2][1]) / 2
            pd.location.z = lp_box[0][2]  # 原点在底部
            # pd.location.z = lp_box[0][2] + obj_dimensions[2] / 2  # 原点在 中心
            all_obj.remove(data)


generate_located(all_locations)

# //TODO  模型z轴摆放设置原点位置问题，在底部得话，设置z轴为定位块下部顶点得z坐标， 在中心得话，设置定位块下部顶点得z坐标 + 模型得z轴寸尺得一半
# //TODO  地板可能因为其中一个定位块占据中间，而导致其他定位块放不进去, 可能有无限循环问题
# //TODO  地板可能本身已有模型，随机定位块，需要防止定位块和已有模型冲突
