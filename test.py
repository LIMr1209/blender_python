import random
from mathutils import Vector
import bpy

ele_obj = ['product.001']
random_count = len(ele_obj)  # 定位立方体数量
floor = bpy.data.objects['floor']  # 地板
floor_location = floor.location  # 地板位置
floor_dimensions = floor.dimensions  # 地板尺寸
# 地板4个顶点 中心点在中心
floor_vertices = [floor.matrix_world @ i.co for i in floor.data.vertices]
direction = 'z'  # 在地板得哪个面放置物体
random_x_l_range = [floor_vertices[0][0], floor_vertices[1][0]]  # x轴取值
random_y_l_range = [floor_vertices[0][1], floor_vertices[2][1]]  # y轴取值



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


pd = bpy.data.objects[ele_obj[0]]
pd_box, dimensions = get_box_list(pd)
obj_dimensions = dimensions
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
name = 'located_0'
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

origin_pd_x_range = [pd_box[0][0], pd_box[4][0]]  # 组合对象外包围框 x轴范围
origin_pd_y_range = [pd_box[0][1], pd_box[2][1]]  # 组合对象外包围框 y轴范围
origin_pd_z_range = [pd_box[0][2], pd_box[1][2]]  # 组合对象外包围框 z轴范围
print(origin_pd_x_range, origin_pd_y_range, origin_pd_z_range)
centre_pd_x = round((origin_pd_x_range[0] + origin_pd_x_range[1]) / 2, 4)  # 组合对象外包围框 x轴中心
centre_pd_y = round((origin_pd_y_range[0] + origin_pd_y_range[1]) / 2, 4)  # 组合对象外包围框 y轴中心
centre_pd_z = round((origin_pd_z_range[0] + origin_pd_z_range[1]) / 2, 4)  # 组合对象外包围框 z轴中心
print(centre_pd_x, centre_pd_y, centre_pd_z)
print(pd.location)
deviation_pd_x = round((pd.location.x - centre_pd_x), 4)  # x原点偏移量
deviation_pd_y = round((pd.location.y - centre_pd_y), 4)  # y原点偏移量
deviation_pd_z = round((pd.location.z - centre_pd_z), 4)  # z原点偏移量
print(deviation_pd_x, deviation_pd_y, deviation_pd_z)
lp_box = [lp.matrix_world @ Vector(lpBvert) for lpBvert in lp.bound_box]  # pd 外边框 8个顶点得xyz全局坐标系
# 这儿会牵扯到 原点位置信息 导致计算位移不准确
pd.location.x = (lp_box[0][0] + lp_box[4][0]) / 2 + deviation_pd_x
pd.location.y = (lp_box[0][1] + lp_box[2][1]) / 2 + deviation_pd_y
# pd.location.z = lp_box[0][2]  # 原点在底部
# pd.location.z = lp_box[0][2] + obj_dimensions[2] / 2 + deviation_pd_z  # 原点在 中心
pd.location.z = (lp_box[0][2] + lp_box[1][2]) / 2 + deviation_pd_z

