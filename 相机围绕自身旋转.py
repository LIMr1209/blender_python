# https://blender.stackexchange.com/questions/253365/how-to-rotate-the-camera-around-itself-using-python
import numpy as np
import mathutils
import math
import bpy


# 旋转矩阵为正交矩阵， 转置和逆相等

# inverted  transposed

def spin_camera():
    cam = bpy.data.objects['Camera']
    location = cam.location.copy()  # 复制位置
    right, up, back = cam.matrix_world.to_3x3().transposed()  # 对象世界矩阵信息提取3x3 旋转矩阵 并转置
    direction = np.cross(up, right)  # 获取相机要查看的方向
    angle = 45
    rotation_vertical = mathutils.Matrix.Rotation(math.radians(angle), 3, mathutils.Vector(direction))
    matrix = rotation_vertical @ cam.matrix_world.to_3x3()
    cam.matrix_world = matrix.to_4x4()
    cam.location = location  # 指定矩阵后，相机将移动到原点，因此有必要再次将其移动到上一个位置。
