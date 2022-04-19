import math

import bpy


def camera_position(matrix):
    t = (matrix[0][3], matrix[1][3], matrix[2][3])
    r = ((matrix[0][0], matrix[0][1], matrix[0][2]),
         (matrix[1][0], matrix[1][1], matrix[1][2]),
         (matrix[2][0], matrix[2][1], matrix[2][2]))
    rp = ((-r[0][0], -r[1][0], -r[2][0]),
          (-r[0][1], -r[1][1], -r[2][1]),
          (-r[0][2], -r[1][2], -r[2][2]))
    output = (rp[0][0] * t[0] + rp[0][1] * t[1] + rp[0][2] * t[2],
              rp[1][0] * t[0] + rp[1][1] * t[1] + rp[1][2] * t[2],
              rp[2][0] * t[0] + rp[2][1] * t[1] + rp[2][2] * t[2])
    return output

import math
for v in bpy.context.window.screen.areas:
    if v.type == 'VIEW_3D':
        L = v.spaces[0].region_3d.view_location
        M = v.spaces[0].region_3d.view_matrix
        R = v.spaces[0].region_3d.view_rotation
        print(R)
        P = camera_position(M)
        print(P)
        cam = bpy.data.cameras.new("Camera")
        cam_ob = bpy.data.objects.new("Camera", cam)
        bpy.context.scene.collection.objects.link(cam_ob)
        bpy.context.scene.camera = cam_ob
        cam_ob.location = P
        cam_ob.rotation_mode = 'QUATERNION'
        cam_ob.rotation_quaternion = R
        cam_ob.rotation_mode = 'XYZ'
        cam_ob.data.sensor_height = 50  # 传感器 适配尺寸 mm 高度
        cam_ob.data.sensor_fit = "VERTICAL"  # 传感器适配方式 垂直
        cam_ob.data.lens_unit = 'FOV'  # 镜头单位  焦距
        cam_ob.data.angle = math.radians(50)
        v.spaces[0].region_3d.view_perspective = 'CAMERA'
