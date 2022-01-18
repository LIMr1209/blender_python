import bpy
from mathutils import Vector
import random

lp = bpy.data.objects["LocatedCube"]
lp1 = bpy.data.objects["LocatedCube.001"]
lp2 = bpy.data.objects["LocatedCube.002"]
lp3 = bpy.data.objects["LocatedCube.003"]
lp4 = bpy.data.objects["LocatedCube.004"]
all_lp = [lp, lp1, lp2, lp3, lp4]


def get_pd_box(obj, pd_box_list):
    for i in obj.children:
        if i.type == 'MESH':
            pd_box_list.extend([i.matrix_world @ Vector(pdBvert) for pdBvert in i.bound_box])
        else:
            for j in i.children:
                pd_box_list = get_pd_box(j, pd_box_list)
    return pd_box_list


for i in ['product', 'product.001']:
    # bpy.ops.object.transform_apply(rotation=True)
    pd = bpy.data.objects[i]
    if pd.type != 'MESH':
        mark = 'group'
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
    else:
        mark = 'single'
        pd_box = [pd.matrix_world @ Vector(pdBvert) for pdBvert in pd.bound_box]  # LocatedCube 外边框 8个顶点得xyz全局坐标系
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
        for i in dimensions_disparity:
            if i['value'] == dimensions_disparity_lp:
                i['name'].append(lp)
                break
        else:
            dimensions_disparity.append({'name': [lp], 'value': dimensions_disparity_lp})
    dimensions_disparity.sort(key=lambda x: x['value'])
    lp_list = dimensions_disparity[0]['name']
    lp = random.choice(lp_list)
    all_lp.remove(lp)
    lp_box = [lp.matrix_world @ Vector(lpBvert) for lpBvert in lp.bound_box]  # pd 外边框 8个顶点得xyz全局坐标系
    pd.location.x = (lp_box[0][0] + lp_box[4][0]) / 2
    pd.location.y = (lp_box[0][1] + lp_box[2][1]) / 2
    if mark == 'single':
        pd.location.z = lp_box[0][2] + pd_d_z / 2
    else:
        pd.location.z = lp_box[0][2]

    # pd.location.x = lp.location.x
    # pd.location.y = lp.location.y
    # pd.location.z = lpBverts[0][2]+pd.dimensions.z/2

