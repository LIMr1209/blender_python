import random

plane_location = [0, 0, 0]  # 位置
plane_dimensions = [40, 40, 0]  # 尺寸
plane_size = 2
direction = 'z'  # 在平面得哪个面放置物体
z_limit = 5
x_limit = 5
y_limit = 5
# 平面4个顶点 中心点在中心
release_range = [
    [plane_location[0] - plane_dimensions[0] / 2, plane_location[1] - plane_dimensions[1] / 2, plane_location[2]],
    [plane_location[0] + plane_dimensions[0] / 2, plane_location[1] - plane_dimensions[1] / 2, plane_location[2]],
    [plane_location[0] + plane_dimensions[0] / 2, plane_location[1] + plane_dimensions[1] / 2, plane_location[2]],
    [plane_location[0] - plane_dimensions[0] / 2, plane_location[1] + plane_dimensions[1] / 2, plane_location[2]],
]
random_count = 5  # 定位立方体数量
random_x_l_range = [plane_location[0] - plane_dimensions[0] / 2, plane_location[0] + plane_dimensions[0] / 2]
random_y_l_range = [plane_location[1] - plane_dimensions[1] / 2, plane_location[1] + plane_dimensions[1] / 2]


def generate_located(random_x_l_range, random_y_l_range):
    dimensions_x = random.randint(0, x_limit)
    dimensions_y = random.randint(0, y_limit)
    dimensions_z = random.randint(0, z_limit)


