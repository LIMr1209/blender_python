from scipy.spatial.transform import Rotation as R
import math

'''
-34.6, 59.0, -63.0
    three.js
        [[ 0.42394657  0.29246115  0.8571673 ]
          [-0.8864592  -0.05998983  0.45890228]
          [ 0.18563241 -0.95439389  0.23382239]]
    blender
    Matrix(((0.23382212221622467, 0.4589025378227234, 0.8571672439575195),
        (-0.18563242256641388, 0.8864590525627136, -0.4239468574523926),
        (-0.9543939828872681, -0.05998987704515457, 0.29246091842651367)))
'''
# three.js 转 blender
origin_r = R.from_euler('zyx', [3.44, 46.41, 9.17], degrees=True)
m = origin_r.as_matrix()


def matrix_convert_three_to_blend(m):
    return [
        [m[2][2], m[1][2], m[0][2]],
        [-m[2][0], -m[1][0], -m[0][0]],
        [m[2][1], m[1][1], m[0][1]],
    ]


new_m = matrix_convert_three_to_blend(m)
r = R.from_matrix(new_m)
print(r.as_euler('xyz', degrees=True))

# blender 脚本
# from mathutils import Euler, Matrix
# from math import radians
#
# m = Euler((radians(-34.6), radians(59.0), radians(float(-63.0))),
#           'ZYX').to_matrix()
# b_m = [m[0], -m[2], m[1]]
# matrix = Matrix(b_m)
# euler = matrix.to_euler('XYZ')

# blender 转 three.js
origin_r = R.from_euler('xyz', [math.degrees(1.6130332946777344), math.degrees(-0.203330859541893),
                                math.degrees(0.8023278713226318)], degrees=True)
m = origin_r.as_matrix()


def matrix_convert_blend_to_three(m):
    return [
        [-m[1][2], m[2][2], m[0][2]],
        [-m[1][1], m[2][1], m[0][1]],
        [-m[1][0], m[2][0], m[0][0]],
    ]


new_m = matrix_convert_blend_to_three(m)
r = R.from_matrix(new_m)
print(r.as_euler('zyx', degrees=True))

origin_r = R.from_euler('xyz', [23, 12, 44], degrees=True)

m = origin_r.as_matrix()
print(m)

from math import *

x, y, z = 23, 12, 44
x, y, z = x * pi / 180, y * pi / 180, z * pi / 180
r11, r12, r13 = cos(z) * cos(y), cos(z) * sin(y) * sin(x) - sin(z) * cos(x), cos(z) * sin(y) * cos(x) + sin(z) * sin(x)
r21, r22, r23 = sin(z) * cos(y), sin(z) * sin(y) * sin(x) + cos(z) * cos(x), sin(z) * sin(y) * cos(x) - cos(z) * sin(x)
r31, r32, r33 = -sin(y), cos(y) * sin(x), cos(y) * cos(x)
print('欧拉角({0:f}, {1:f}, {2:f})转换为旋转矩阵'.format(x * 180 / pi, y * 180 / pi, z * 180 / pi))
print('{0:f} , {1:f} , {2:f}'.format(r11, r12, r13))
print('{0:f} , {1:f} , {2:f}'.format(r21, r22, r23))
print('{0:f} , {1:f} , {2:f}'.format(r31, r32, r33))
