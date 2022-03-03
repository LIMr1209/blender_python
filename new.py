import bpy
from mathutils import Vector

model_path = r'C:\Users\thn\Desktop\product5.glb'

bpy.ops.import_scene.gltf(filepath=model_path)

model = bpy.context.selected_objects[:]
for i in model:
    if i.type != "EMPTY":
        i.name = "product"
        bpy.context.view_layer.objects.active = i
        break

bpy.ops.object.join()
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

pdc = bpy.data.objects["ProductContainer"]
pd = bpy.data.objects["product"]
lp = bpy.data.objects["LocatedCube"]
pd.parent = pdc

k1 = pd.dimensions.x
k2 = pd.dimensions.y
k3 = pd.dimensions.z
dimList = [k1, k2, k3]
k = max(dimList)
v = lp.dimensions.y

pd.scale *= v / k
bpy.context.view_layer.update()
pdBverts = [pd.matrix_world @ Vector(pdBvert) for pdBvert in pd.bound_box]
lpBverts = [lp.matrix_world @ Vector(lpBvert) for lpBvert in lp.bound_box]

pd.location = lpBverts[3] - pdBverts[3]
pd.select_set(True)
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
pd.location.z -= pd.dimensions.z
camera = bpy.data.objects['Camera']
# 相机动画渲染视频
scene = bpy.context.scene
scene.frame_end = 140  # 结束帧
scene.frame_start = 20  # 起始帧
frame_rate = 24
F = bpy.data.objects['LocatedCube']

scene.frame_set(scene.frame_start)
camera.data.dof.use_dof = True
camera.data.dof.focus_object = F
camera.data.dof.aperture_fstop = 1.4
track_to = camera.constraints.new(type='TRACK_TO')
track_to.target = F

frame_range = scene.frame_end - scene.frame_start
marker = scene.timeline_markers.new('')
marker.frame = 20
marker.camera = camera

current_set = scene.frame_start

step_1_s = 3
default_location_camera = camera.location[0]
step_1_f = step_1_s * frame_rate
intercept_num = 5 / step_1_f

left_location = default_location_camera - 5
for i in range(step_1_f):
    camera.location[0] = left_location
    camera.keyframe_insert(data_path="location", frame=current_set)
    left_location = left_location + intercept_num
    current_set += 1

step_2_s = 2
default_fov_camera = camera.data.lens
step_2_f = step_2_s * frame_rate
intercept_num = 10 / step_2_f
camera.data.keyframe_insert(data_path="lens", frame=current_set-1)
camera.data.lens = default_fov_camera - 10
camera.data.keyframe_insert(data_path="lens", frame=current_set)
for i in range(step_1_f):
    current_set += 1
    camera.data.lens -= intercept_num
    camera.data.keyframe_insert(data_path="lens", frame=current_set)

step_3_s = 2.5
current_set = int(step_3_s * frame_rate)
intercept_num = pd.dimensions.z / (scene.frame_end - current_set)
for i in range(current_set, scene.frame_end):
    pd.location.z += intercept_num
    pd.keyframe_insert(data_path="location", frame=current_set)
    current_set += 1
