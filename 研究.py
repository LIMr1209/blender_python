import bpy
from mathutils import Vector

bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
pd = bpy.data.objects["product"]
lp = bpy.data.objects["LocatedCube"]

# 适配缩放
k1 = pd.dimensions.x
k2 = pd.dimensions.y
k3 = pd.dimensions.z
dimList = [k1, k2, k3]
k = max(dimList)
v = lp.dimensions.y

# 适配位移
pdBverts = [pd.matrix_world @ Vector(pdBvert) for pdBvert in pd.bound_box] # LocatedCube 外边框 8个顶点得xyz全局坐标系
lpBverts = [lp.matrix_world @ Vector(lpBvert) for lpBvert in lp.bound_box] # pd 外边框 8个顶点得xyz全局坐标系

pd.location = lpBverts[3] - pdBverts[3]  # 8个顶点  选择第三个节点适配位移

pd.select_set(True)
bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)
