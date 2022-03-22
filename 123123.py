import bpy
cube_name = 'default_f'
camera_times_num = 12
target_num = 12
render_file_path = './'

# 选中物体
cube = bpy.data.objects[cube_name]
camera = bpy.data.objects['default_camera']
default_location_camera = camera.location[0]
track_to = camera.constraints.new(type='TRACK_TO')
# 添加约束
track_to.target = cube
camera_num = camera_times_num / 2  # 总长度除以2
intercept_num = camera_times_num / target_num  # 总长度 / 截取次数 = 移动目标x位置
camera_position = camera_num - default_location_camera  # 摄像初始位置
bpy.context.scene.render.image_settings.file_format = "JPEG"
bpy.context.scene.render.resolution_percentage = 100
for d in range(target_num):
    # 物体位置
    bpy.context.scene.frame_set(d + 1)
    camera.location[0] = -camera_position
    camera.keyframe_insert(data_path="location")
    print(camera.location[0])
    camera_position = camera_num - intercept_num - default_location_camera  # 摄像位置
    bpy.context.view_layer.update()
    camera_num -= intercept_num