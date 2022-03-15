import bpy
from mathutils import Vector
import random

# 定位块 更新 transform  矩阵没有立即更新  使用 bpy.context.view_layer.update() 更新矩阵 https://blender.stackexchange.com/questions/27667/incorrect-matrix-world-after-transformation
lp = bpy.data.objects["location_001"]
lp1 = bpy.data.objects["location_002"]
lp2 = bpy.data.objects["location_003"]
all_lp = [lp, lp1, lp2]
pd_list = ['cup_001', 'cup_002', 'coffee_maker_001']


def get_pd_box(obj, pd_box_list):
    if obj.type == 'MESH':
        pd_box_list.extend([obj.matrix_world @ Vector(pdBvert) for pdBvert in obj.bound_box])
    for i in obj.children:
        pd_box_list = get_pd_box(i, pd_box_list)
    return pd_box_list


for i in pd_list:
    # bpy.ops.object.transform_apply(rotation=True)
    try:
        pd = bpy.data.objects[i]
    except:
        continue
    # 是否可以把子级面板 join 合成一个面板 bpy.ops.object.join()
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
    # pd_d_x = pd.dimensions.x
    # pd_d_y = pd.dimensions.y
    # pd_d_z = pd.dimensions.z
    dimensions_disparity = []
    for lp in all_lp:
        # 如果其中一个轴得尺寸小于产品尺寸， 产品模型放不进去
        if lp.dimensions.x < pd_d_x or lp.dimensions.y < pd_d_y or lp.dimensions.z < pd_d_z:
            continue
        dimensions_disparity_lp = round(abs(pd_d_x - lp.dimensions.x) + abs(pd_d_y - lp.dimensions.y) + abs(
            pd_d_z - lp.dimensions.z), 2)
        for j in dimensions_disparity:
            if j['value'] == dimensions_disparity_lp:
                j['name'].append(lp)
                break
        else:
            dimensions_disparity.append({'name': [lp], 'value': dimensions_disparity_lp})
    if not dimensions_disparity:
        continue
    dimensions_disparity.sort(key=lambda x: x['value'])
    lp_list = dimensions_disparity[0]['name']
    lp = random.choice(lp_list)
    all_lp.remove(lp)
    lp_box = [lp.matrix_world @ Vector(lpBvert) for lpBvert in lp.bound_box]  # pd 外边框 8个顶点得xyz全局坐标系
    # 这儿会牵扯到 原点位置信息 导致计算位移不准确
    pd.location.x = (lp_box[0][0] + lp_box[4][0]) / 2
    pd.location.y = (lp_box[0][1] + lp_box[2][1]) / 2
    pd.location.z = lp_box[0][2]  # 原点在底部
    # pd.location.z = lp_box[0][2] + pd_d_z / 2  # 原点在 中心
