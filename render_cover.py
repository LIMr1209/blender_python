import bpy
from mathutils import Vector

# 等比缩放 2, 设置物体原点为 物体外边框正中心， 设置坐标为0，0，0
appropriate_dimensions = 9.6

obj = bpy.data.objects['product2trans']

k1 = obj.dimensions.x
k2 = obj.dimensions.y
k3 = obj.dimensions.z
dimList = [k1, k2, k3]
k = max(dimList)

obj.scale *= appropriate_dimensions / k

pd_box = [obj.matrix_world @ Vector(pdBvert) for pdBvert in obj.bound_box]
x = (pd_box[0][0] + pd_box[4][0]) / 2
y = (pd_box[0][1] + pd_box[2][1]) / 2
z = (pd_box[0][2] + pd_box[1][2]) / 2
bpy.context.scene.cursor.location = x, y, z
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
obj.location = 0, 0, 0
obj.rotation_mode = 'XYZ'
obj.rotation_euler = (0.143621563911438, -0.013038791716098785, 0.608063817024231)
bpy.context.scene.cursor.location = 0, 0, 0
