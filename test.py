from scipy.spatial.transform import Rotation as R

origin_r = R.from_euler('zyx', [-34.6, 59.0, -63.0], degrees=True)
m = origin_r.as_matrix()

# Euler((radians(-34.6), radians(59.0), radians(-63.0)), 'zyx').to_matrix()

print(m)
'''
    three.js
        0.2338223930133095,
        -0.9543938894679361,
        0.18563241169524922,
        0.4589022849502757,
        -0.05998983159917603,
        -0.8864591998350059,
        0.8571673007021124,
        0.2924611493018649,
        0.4239465706384317,
    blender  
    Matrix(((0.23382212221622467, 0.4589025378227234, 0.8571672439575195),
        (-0.18563242256641388, 0.8864590525627136, -0.4239468574523926),
        (-0.9543939828872681, -0.05998987704515457, 0.29246091842651367)))
'''


def convert_matrix(m):
    return [[m[2][2], m[1][2], m[0][2]],
            [-m[2][0], -m[1][0], -m[0][0]],
            [m[2][1], m[1][1], m[0][1]],
            ]


new_m = convert_matrix(m)
print(new_m)
r = R.from_matrix(new_m)
print(r.as_euler('xyz', degrees=True))

# from mathutils import Euler, Matrix
# from math import radians
#
# m = Euler((radians(-34.6), radians(59.0), radians(float(-63.0))),
#           'ZYX').to_matrix()
# b_m = [m[0], -m[2], m[1]]
# matrix = Matrix(b_m)
# euler = matrix.to_euler('XYZ')

