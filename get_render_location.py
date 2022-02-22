# 获取模型 顶点 渲染后对应得图片所在得像素点
import bpy
import bpy_extras

scene = bpy.context.scene
obj = bpy.data.objects['Cube']
vertices = obj.data.vertices  # 获取模型顶点
camera = scene.camera

for v in vertices:
    co = obj.matrix_world @ v.co  # 顶点局部坐标 转换为全局坐标
    co_2d = bpy_extras.object_utils.world_to_camera_view(scene, camera, co)  # 计算二维图像坐标
    render_scale = scene.render.resolution_percentage / 100
    render_size = (
        int(scene.render.resolution_x * render_scale),
        int(scene.render.resolution_y * render_scale),
    )
    # this is the result
    pixel_coords = (co_2d.x * render_size[0], co_2d.y * render_size[1])
    print("Pixel Coords:", (
        round(pixel_coords[0]),
        round(pixel_coords[1]),
    ))
