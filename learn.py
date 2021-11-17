import bpy
import math
import mathutils

'''
角度和弧度关系是：2π 弧度 = 360°。从而 1°≈0.0174533 弧度，1 弧度≈57.29578°。

1) 角度转换为弧度公式：弧度=角度÷180×π
2) 弧度转换为角度公式： 角度=弧度×180÷π
'''
# math.degrees(1.2420707941055298)  # 将弧度转换为角度。
# math.radians(60)  # 将角度转换为弧度。
pi = 3.14159265
'''
选择：可以同时选择一个、多个或零个对象。使用选定对象的操作可以同时对单个对象或多个对象执行该操作。
激活：在任何给定时间，只有一个对象可以处于活动状态。对活动对象执行操作的操作通常更具体、更激烈，因此无法同时直观地对许多操作执行。
规范：（仅限 Python）Python 脚本可以通过对象的名称访问对象，并直接写入其数据块。虽然操作选定对象的操作通常是一种差异操作，如平移、旋转或缩放，但将数据写入特定对象通常是一种声明性操作，如位置、方向或大小。
'''

# 选择物体
bpy.data.objects["Cube"].select_set(True)
# 取消所有选择
bpy.ops.object.select_all(action='DESELECT')
# 选中所有物体
bpy.ops.object.select_all(action='SELECT')
# 激活物体
bpy.context.view_layer.objects.active = bpy.data.objects['Cube']

'''
在blender中存在着选中和激活两种状态。什么叫做激活？在blender中只能使一个物体处于激活状态，界面中被激活的物体上会有一个小蓝点，在显示窗口的右下角也会显示当前被激活物体的名称。
当只选中了一个物体时，该物体既被选中又被激活，而当选中多个物体时，只有第一个选中的物体为激活状态。
'''
# 显示选择的物体
bpy.context.selected_objects
# 显示激活的物体名称
bpy.context.object

# 移动所有选择的物体 在原来的基础上
'''
bpy.ops.transform.translate(value=(0, 0, 0), orient_type='GLOBAL', orient_matrix=((0, 0, 0), (0, 0, 0), (0, 0, 0)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, cursor_transform=False, texture_space=False, remove_on_cancel=False, release_confirm=False, use_accurate=False, use_automerge_and_split=False)
Move selected items
'''
bpy.ops.transform.translate(value=(2, 2, 2), constraint_axis=(True, True, True))
# 缩放所有选择的物体 在原来的基础上
'''
bpy.ops.transform.resize(value=(1, 1, 1), orient_type='GLOBAL', orient_matrix=((0, 0, 0), (0, 0, 0), (0, 0, 0)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, texture_space=False, remove_on_cancel=False, center_override=(0, 0, 0), release_confirm=False, use_accurate=False)
Scale (resize) selected items
'''
bpy.ops.transform.resize(value=(2, 2, 2), constraint_axis=(True, True, True))
# 指定轴旋转所有选择的物体弧度 在原来的基础上
'''
bpy.ops.transform.rotate(value=0, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((0, 0, 0), (0, 0, 0), (0, 0, 0)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, False), mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False, snap=False, snap_target='CLOSEST', snap_point=(0, 0, 0), snap_align=False, snap_normal=(0, 0, 0), gpencil_strokes=False, center_override=(0, 0, 0), release_confirm=False, use_accurate=False)
Rotate selected items
'''
bpy.ops.transform.rotate(value=45, orient_axis='X')

# 激活物体指定坐标
bpy.context.object.location = (1, 1, 1)
# 激活物体指定缩放值
bpy.context.object.scale = (0.5, 0.5, 0.5)
# 激活物体指定弧度
bpy.context.object.rotation_euler = (45 * (pi / 180.0), 45 * (pi / 180.0), 45 * (pi / 180.0))  # 45 度
# 激活物体重命名
bpy.context.object.name = 'new_name'

# 规范物体的位置值改变
bpy.data.objects["Cube"].location = (2, 2, 2)
# 规范物体的缩放值改变
bpy.data.objects["Cube"].scale = (0.5, 0.5, 0.5)
# 规范物体的旋转弧度值改变
bpy.data.objects["Cube"].rotation_euler = (45 * (pi / 180.0), 45 * (pi / 180.0), 45 * (pi / 180.0))  # 45 度

# 变换增量
bpy.data.objects["Cube"].delta_location = (2, 2, 2)  # 更新位置
bpy.data.objects["Cube"].delta_scale = (0.5, 0.5, 0.5)  # 更新大小比例
bpy.data.objects["Cube"].rotation_mode = 'YZX'  # 旋转模式      YZX 和 threejs 统一 x 轴相同 y 轴等于 -z z 轴 等于 y轴
bpy.data.objects["Cube"].delta_rotation_euler = (45 * (pi / 180.0), 45 * (pi / 180.0), 45 * (pi / 180.0))  # 45 度 更新欧拉旋转

# 添加一个立方体 并选中 激活
bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, 0, 0))

# 添加一个球体 并选中 激活
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(0, 0, 0))

# 添加一个圆锥 并选中 激活
bpy.ops.mesh.primitive_cone_add(radius1=0.5, location=(0, 0, 0))

# 删除选中的所有物体
bpy.ops.object.delete(use_global=False)

# 删除物体
# https://blender.stackexchange.com/questions/27234/python-how-to-completely-remove-an-object
objs = [ob for ob in bpy.context.scene.objects if ob.type in ('CAMERA', 'POINT', 'EMPTY')]
bpy.ops.object.delete({"selected_objects": objs})


# 删除层级
# https://blender.stackexchange.com/questions/44653/delete-parent-object-hierarchy-in-code/44786
def delete_hierarchy(parent_obj_name):
    obj = bpy.data.objects[parent_obj_name]
    obj.animation_data_clear()
    objs = set()

    # Go over all the objects in the hierarchy like @zeffi suggested:
    def get_child_names(obj):
        for child in obj.children:
            objs.add(child)
            if child.children:
                get_child_names(child)

    get_child_names(obj)
    # Remove the animation from the all the child objects
    for obj in objs:
        obj.animation_data_clear()

    bpy.ops.object.delete({"selected_objects": objs})


'''
切换到编辑模式时，此时激活的对象将是用户可以在该编辑模式会话中编辑的唯一对象。如果用户要在编辑模式下操作不同的对象，则必须先切换回对象模式以激活所需的对象。只有在切换回编辑模式并激活所需对象后，他才能对其进行操作
'''

# 切换编辑模式
bpy.ops.object.mode_set(mode="EDIT")
# 切换对象模式
bpy.ops.object.mode_set(mode="OBJECT")

# 导出
bpy.ops.export_scene.obj(filepath='')  # obj
bpy.ops.export_scene.gltf(filepath='')  # gltf
bpy.ops.export_scene.x3d(filepath='')  # x3d
bpy.ops.export_scene.fbx(filepath='')  # fbx

# 导入
bpy.ops.import_scene.obj(filepath='')  # obj
bpy.ops.import_scene.gltf(filepath='')  # gltf
bpy.ops.import_scene.x3d(filepath='')  # x3d
bpy.ops.import_scene.fbx(filepath='')  # fbx

# 保存blender
bpy.ops.wm.save_mainfile(filepath='')
# 打开blender
bpy.ops.wm.open_mainfile(filepath='')
# 追加blender文件内对象
import os

file_path = r'C:\Users\thn\Desktop\blender\test.blend'
inner_path = 'Object'
object_name = 'Cube'

bpy.ops.wm.append(
    filepath=os.path.join(file_path, inner_path, object_name),
    directory=os.path.join(file_path, inner_path),
    filename=object_name
)

# 执行python 脚本文件
bpy.ops.script.python_file_run(filepath='')

# 用户设置cycles 渲染引擎开启使用CUDA
bpy.context.preferences.addons["cycles"].preferences.compute_device_type = "CUDA"

# 检测 CUDA 和 OpenCL 设备：
cuda_devices, opencl_devices = bpy.context.preferences.addons['cycles'].preferences.get_devices()
# 为 CUDA 启用所需的设备
bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'
for device in bpy.context.preferences.addons['cycles'].preferences.devices:
    device.use = True
# 用于 OpenCL
bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'OpenCL'
for device in bpy.context.preferences.addons['cycles'].preferences.devices:
    device.use = True
# 用于 OPTIX
bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'OPTIX'
for device in bpy.context.preferences.addons['cycles'].preferences.devices:
    device.use = True

# 打印用户设置的cycles 设备使用项
bpy.context.preferences.addons["cycles"].preferences.compute_device_type

# 并且具体场景渲染选项cycles 渲染设备选择GPU
bpy.context.scene.cycles.device = "GPU"

bpy.ops.preferences.addon_enable(module='render_auto_tile_size')
bpy.ops.preferences.addon_disable(module='render_auto_tile_size')
bpy.ops.wm.save_userpref()

# 设置tile size
bpy.context.scene.cycles.tile_order = "RIGHT_TO_LEFT"
bpy.context.scene.render.tile_x = 32
bpy.context.scene.render.tile_y = 32

bpy.context.scene.cycles.samples = 256  # 采样数量

# 渲染相关
bpy.context.scene.frame_set(200)  # 指定关键帧渲染图片
bpy.data.scenes["Scene"].render.image_settings.file_format = 'PNG'  # 渲染保存文件格式
bpy.data.scenes["Scene"].render.filepath = ''  # 保存文件路径
bpy.ops.render.render(write_still=True)  # 渲染保存

# 制作动画
# 1，选择帧
bpy.context.scene.frame_set(200)
# 设置当前物体变幻数值
bpy.context.object.scale = (0.5, 0.5, 0.5)
# frame 为指定帧，默认当前帧frame_set, index 变换的数据索引，默认-1，所有索引, 如 index=0, 变换仅变换x轴
bpy.context.object.keyframe_insert('rotation_euler', frame=200, index=-1)
# 渲染
bpy.data.scenes["Scene"].render.image_settings.file_format = 'AVI_JPEG'  # 渲染保存文件格式
bpy.data.scenes["Scene"].render.resolution_x = 1920  # 分辨率 x
bpy.data.scenes["Scene"].render.resolution_y = 1080  # 分辨率 y
bpy.data.scenes["Scene"].render.resolution_percentage = 100  # 渲染分辨率的缩放比例
bpy.data.scenes["Scene"].frame_end = 200  # 结束帧
bpy.data.scenes["Scene"].frame_start = 0  # 起始帧
bpy.data.scenes["Scene"].frame_step = 2  # 步长
bpy.data.scenes["Scene"].render.filepath = ''  # 保存文件路径
# https://blender.stackexchange.com/questions/106659/change-encoding-settings-through-python-api
bpy.data.scenes["Scene"].render.image_settings.file_format = 'FFMPEG'
bpy.data.scenes["Scene"].render.ffmpeg.constant_rate_factor = 'HIGH'
bpy.data.scenes["Scene"].render.ffmpeg.format = 'MPEG4'
bpy.ops.render.render(animation=True)  # 渲染保存

# 添加相机
camera_data = bpy.data.cameras.new(name='Camera')
camera_object = bpy.data.objects.new('Camera', camera_data)
bpy.context.scene.collection.objects.link(camera_object)
# 相机
bpy.data.objects['Camera'].data.type = 'PERSP'  # ('PERSP', 'ORTHO', 'PANO')  相机类型 默认透视
bpy.data.objects['Camera'].data.lens_unit = 'MILLIMETERS'  # ('MILLIMETERS', 'FOV') 镜头单位 默认毫米（焦距）   视野（度数）
bpy.data.objects['Camera'].data.shift_x = 0.0  # x 向移位
bpy.data.objects['Camera'].data.shift_y = 0.0  # y 向移位
bpy.data.objects['Camera'].data.clip_start = 0.1  # 裁剪起点
bpy.data.objects['Camera'].data.clip_end = 100  # 裁剪终点
bpy.data.objects['Camera'].data.angle = 60 * (pi / 180.0)  # 视野度数 60
bpy.data.objects['Camera'].data.angle = math.radians(60)  # 视野度数 60
bpy.data.objects['Camera'].data.lens = 31.18  # 焦距 mm
bpy.data.objects['Camera'].data.sensor_fit = 'VERTICAL'  # ('AUTO', 'HORIZONTAL', 'VERTICAL') 传感器适配方式
bpy.data.objects['Camera'].data.sensor_width = 36  # 传感器 适配尺寸 mm 宽度
bpy.data.objects['Camera'].data.sensor_height = 50  # 传感器 适配尺寸 mm 高度

# 添加标准跟随约束
target_obj = bpy.data.objects['Cube']
camera_obj = bpy.data.objects['Camera']

constraint = camera_obj.constraints.new(type='TRACK_TO')
constraint.target = target_obj
# 移动目标物体， camera_obj 应用可视变换,更新变换信息
bpy.ops.object.visual_transform_apply()  # 应用可视变换
camera_obj.constraints.remove(constraint)  # 删除变换


# 获取帧绑定的相机标记
# https://blender.stackexchange.com/questions/43764/bind-camera-to-marker-via-python
def get_frame_camera(frame):
    all_markers = bpy.context.scene.timeline_markers
    for i in all_markers:
        if i.frame == frame:
            return i.camera


# 相机焦距 转换 视野 公式
lens = 31.18
sensor_width = 36
angle = math.degrees(2 * math.atan(sensor_width / (2 * lens)))

# 旋转模式 转化

# https://blender.stackexchange.com/questions/152893/changing-rotation-mode-from-yxz-to-xyz-without-changing-orientation

ob = bpy.context.active_object

x, y, z = 1, 2, 3

rot_YXZ = mathutils.Euler((x, y, z), 'YXZ')
rot_mat = rot_YXZ.to_matrix()
rot_XYZ = rot_mat.to_euler('XYZ')

ob.rotation_mode = 'XYZ'
ob.rotation_euler = rot_XYZ

# 启动 crowdrender
# ./blender -noaudio -b --python ~/.config/blender/2.93/scripts/addons/crowdrender/src/cr/serv_int_start.py -- -t "server_int_proc"
#
