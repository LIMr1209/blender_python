import bpy

camera_times_num = 14
scene = bpy.context.scene
F = bpy.data.objects['default_f']

scene.frame_set(0)
video_camera = bpy.data.objects['default_camera'].copy()
video_camera.data = bpy.data.objects['default_camera'].data.copy()
video_camera.name = 'vid_camera'
video_camera.data.dof.use_dof = True
video_camera.data.dof.focus_object = F
video_camera.data.dof.aperture_fstop = 1.4
bpy.context.collection.objects.link(video_camera)
track_to = video_camera.constraints.new(type='TRACK_TO')
track_to.target = F

scene.frame_end = 140  # 结束帧
scene.frame_start = 20  # 起始帧
frame_range = scene.frame_end - scene.frame_start
marker = scene.timeline_markers.new('')
marker.frame = 20
marker.camera = video_camera

current_set = scene.frame_start
default_location_camera = video_camera.location[0]

step_1 = int(frame_range / 3 * 2)
camera_num = (camera_times_num / 2)  # 总长度除以2
intercept_num = camera_times_num / step_1  # 总长度 / 截取次数 = 移动目标x位置
camera_position = camera_num - default_location_camera  # 摄像初始位置
for d in range(step_1):
    video_camera.location[0] = -camera_position
    video_camera.keyframe_insert(data_path="location", frame=current_set)
    camera_position = camera_num - intercept_num - default_location_camera  # 摄像位置
    camera_num -= intercept_num
    current_set += 1

step_2 = int((int(frame_range / 3 * 2)) / 2)
camera_num_1 = -camera_position
intercept_num_1 = camera_times_num / step_2 / 2
camera_position_1 = camera_num_1
for m in range(step_2):
    video_camera.location[0] = camera_position_1
    print(camera_position_1)
    video_camera.keyframe_insert(data_path="location", frame=current_set)
    camera_position_1 = camera_num_1 - intercept_num_1   # 摄像位置
    camera_num_1 -= intercept_num_1
    current_set += 1

bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'OPTIX'
bpy.context.preferences.addons["cycles"].preferences.get_devices()
for device in bpy.context.preferences.addons['cycles'].preferences.devices:
    device.use = True
bpy.context.scene.render.image_settings.file_format = "FFMPEG"
bpy.context.scene.render.ffmpeg.constant_rate_factor = "HIGH"
bpy.context.scene.render.ffmpeg.format = "MPEG4"
bpy.context.scene.render.resolution_percentage = 100

cube = bpy.data.objects['default_f']
bpy.context.scene.frame_set(0)
camera = bpy.data.objects['default_camera']
default_location_camera = camera.location[0]
camera_times_num = 14
target_num = 12
render_file_path = 'E:/Python/'
track_to = camera.constraints.new(type='TRACK_TO')
track_to.target = cube
camera_num = (camera_times_num / 2)  # 总长度除以2
intercept_num = camera_times_num / target_num  # 总长度 / 截取次数 = 移动目标x位置
camera_position = camera_num - default_location_camera  # 摄像初始位置
bpy.context.scene.render.image_settings.file_format = "JPEG"
bpy.context.scene.render.resolution_percentage = 100
for d in range(target_num):
    camera.location[0] = -camera_position
    camera.keyframe_insert(data_path="location", frame=0)
    camera_position = camera_num - intercept_num - default_location_camera  # 摄像位置
    camera_num -= intercept_num
    # 渲染图像
    path = '%s%s.jpg' % (render_file_path, d)
    bpy.context.scene.render.filepath = path
    bpy.ops.render.render(write_still=True)
