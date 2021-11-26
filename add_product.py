import argparse
import sys
import bpy
import math
from mathutils import Vector, Matrix, Euler
import json


def get_frame_camera(frame):
    """
    获取帧绑定的相机标记
    """
    all_markers = bpy.context.scene.timeline_markers
    for i in all_markers:
        if i.frame == frame:
            return i.camera


def add_product_old(model_path):
    """
    场景添加产品
    :param model_path: 产品模型路径
    :return:
    """

    bpy.ops.import_scene.gltf(filepath=model_path)

    model = bpy.context.selected_objects[:]
    bpy.context.view_layer.objects.active = model[0]
    model[0].name = "product"
    bpy.ops.object.join()
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)

    bpy.ops.object.empty_add(
        type="PLAIN_AXES", align="WORLD", location=(0, 0, 0), scale=(1, 1, 1)
    )
    bpy.context.object.name = "ProductContainer"

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

    pdBverts = [pd.matrix_world @ Vector(pdBvert) for pdBvert in pd.bound_box]
    lpBverts = [lp.matrix_world @ Vector(lpBvert) for lpBvert in lp.bound_box]

    pd.location = lpBverts[3] - pdBverts[3]
    pd.select_set(True)
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)

    pdBverts = [pd.matrix_world @ Vector(pdBvert) for pdBvert in pd.bound_box]
    lpBverts = [lp.matrix_world @ Vector(lpBvert) for lpBvert in lp.bound_box]

    pd.location = lpBverts[3] - pdBverts[3]
    pd.select_set(True)
    bpy.ops.object.transform_apply(location=True, rotation=False, scale=False)


def remove_empty():
    """
    删除空对象
    """
    while True:
        model = bpy.context.selected_objects[:]
        # 删除空物体
        objs = [
            i
            for i in model
            if i.type in ["EMPTY", "LIGHT", "CAMERA"] and not i.children
        ]
        bpy.ops.object.delete({"selected_objects": objs})
        if not objs:
            break


def add_product_old_2(model_path):
    """
    场景添加产品
    :param model_path: 产品模型路径
    :return:
    """

    bpy.ops.import_scene.gltf(filepath=model_path)

    model = bpy.context.selected_objects[:]
    model[0].name = "product"
    bpy.context.view_layer.objects.active = model[0]
    bpy.ops.object.join()
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    # bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    # bpy.context.object.name = "ProductContainer"
    #
    # pdc = bpy.data.objects['ProductContainer']
    # pd = bpy.data.objects['product']
    # pd.parent = pdc


def add_product(model_path):
    """
    场景添加产品
    :param model_path: 产品模型路径
    :return:
    """

    bpy.ops.import_scene.gltf(filepath=model_path)

    # 删除空对象
    remove_empty()
    # 组合
    model = bpy.context.selected_objects[:]
    for i in model:
        if i.type != "EMPTY":
            i.name = "product"
            bpy.context.view_layer.objects.active = i
            break
    bpy.ops.object.join()
    # 删除空对象
    remove_empty()
    # 应用变换
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    # 清除动画
    model = bpy.context.selected_objects[:]
    for i in model:
        i.animation_data_clear()

    name_index = 0
    while True:
        pd = bpy.data.objects['product']
        parent = pd.parent
        if parent:
            name_index += 1
            pd.name = 'product.' + str(name_index).zfill(4)
            parent.name = 'product'
        else:
            break
    # 建立空的父对象 对父对象进行 变换
    bpy.ops.object.empty_add(
        type="PLAIN_AXES", align="WORLD", location=(0, 0, 0), scale=(1, 1, 1)
    )
    bpy.context.object.name = "ProductContainer"
    pd = bpy.data.objects["product"]
    pdc = bpy.data.objects["ProductContainer"]
    pd.parent = pdc


def add_product_new(model_path):
    """
    场景添加产品
    :param model_path: 产品模型路径
    :return:
    """

    bpy.ops.import_scene.gltf(filepath=model_path)

    # 删除空对象
    remove_empty()
    # 清除动画
    model = bpy.context.selected_objects[:]
    for i in model:
        i.animation_data_clear()
    # 建立空的父对象 对父对象进行 变换
    bpy.ops.object.empty_add(
        type="PLAIN_AXES", align="WORLD", location=(0, 0, 0), scale=(1, 1, 1)
    )
    bpy.context.object.name = "ProductContainer"
    pdc = bpy.data.objects["ProductContainer"]
    for i in model:
        if not i.parent:
            i.parent = pdc


def update_transform(location, scale, rotation_euler):
    """
    更新变换信息
    :param location: 位置
    :param scale: 大小比例
    :param rotation_euler: 欧拉旋转
    :return:
    """
    pd = bpy.data.objects["ProductContainer"]
    pd.location = location  # 更新位置
    # pd.delta_location = location  # 更新位置
    # pd.delta_scale = scale  # 更新大小比例
    pd.scale = scale  # 更新大小比例
    pd.rotation_mode = "YZX"  # 旋转模式
    # pd.delta_rotation_euler = rotation_euler  # 更新欧拉旋转
    pd.rotation_euler = rotation_euler  # 更新欧拉旋转


def update_camera(camera_option):
    """
    更新摄像头信息
    :param camera_option: 相机信息
    :return:
    """
    for i in range(len(camera_option)):
        try:
            # camera = get_frame_camera(camera_option[i]['frame'])
            camera = get_frame_camera(i + 1)
            # camera = bpy.data.cameras[camera_option[i]["name"]]
        except:
            continue
        if camera:
            camera.name = camera_option[i]["name"]
            camera.data.sensor_height = 50  # 传感器 适配尺寸 mm 高度
            camera.data.sensor_fit = "VERTICAL"  # 传感器适配方式 垂直
            camera.data.lens_unit = 'FOV'  # 镜头单位  焦距
            camera.data.angle = math.radians(float(camera_option[i]["fov"]))
            camera.data.clip_start = float(camera_option[i]["near"])
            camera.data.clip_end = float(camera_option[i]["far"])
            camera.location = camera_option[i]["location"]
            # camera.rotation_mode = "YZX"
            # camera.rotation_euler = camera_option[i]["rotate"]
            rotate = camera_option[i]["rotate"]
            m = Euler((float(rotate[0]), float(rotate[1]), float(rotate[2])),
                      'ZYX').to_matrix()
            b_m = [m[0], -m[2], m[1]]
            matrix = Matrix(b_m)
            euler = matrix.to_euler('XYZ')
            camera.rotation_mode = "XYZ"
            camera.rotation_euler = euler


def update_material(material_option):
    """
    更新材质信息
    :param material_option: 材质信息
    :return:
    """
    for j, i in enumerate(material_option):
        obj = bpy.data.objects[i.pop('obj_name')]
        mat = obj.active_material
        if not mat:
            mat = bpy.data.materials.new(name='mat.' + str(j).zfill(4))  # 创建材质
            obj.active_material = mat  # 设置物体激活的材质
        if mat.node_tree:
            mat.node_tree.links.clear()  # 节点树中删除所有节点链接
            mat.node_tree.nodes.clear()  # 节点树中删除所有节点
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        output = nodes.new(type='ShaderNodeOutputMaterial')
        shader = nodes.new(type='ShaderNodeBsdfPrincipled')  # 原理化BSDF
        links.new(shader.outputs[0], output.inputs[0])  # 将节点链接添加到此节点树
        for z, y in i.items():
            # 颜色 RGB 转换
            if z in ['base_color', 'subsurface_color', 'emission']:
                y = [i / 255.0 for i in y[:3]] + y[-1:]
            if z == 'ior':
                z = 'IOR'
            else:
                temp = [i.capitalize() for i in z.split('_')]
                z = ' '.join(temp)
            shader.inputs[z].default_value = y


def update_output(of, pixel):
    """
    更新输出选项
    :param of: jpeg 或者 mp4
    :param pixel: 像素分辨率
    :return:
    """
    if pixel and pixel != (0, 0):
        bpy.context.scene.render.resolution_x = pixel[0]  # 分辨率 x
        bpy.context.scene.render.resolution_y = pixel[1]  # 分辨率 y
    if of == "jpeg":
        bpy.context.scene.render.image_settings.file_format = "JPEG"
        bpy.context.scene.cycles.samples = 64
        bpy.context.scene.render.resolution_percentage = 100
    elif of == "ffmpeg":
        bpy.context.scene.render.image_settings.file_format = "FFMPEG"
        bpy.context.scene.render.ffmpeg.constant_rate_factor = "HIGH"
        bpy.context.scene.render.ffmpeg.format = "MPEG4"
        bpy.context.scene.cycles.samples = 64
        bpy.context.scene.render.resolution_percentage = 100


class ArgumentParserForBlender(argparse.ArgumentParser):
    """
    获取blender 传给python 脚本的参数
    """

    def listRightIndex(self, alist, value):
        return len(alist) - alist[-1::-1].index(value) - 1

    def _get_argv_after_doubledash(self):
        try:
            idx = self.listRightIndex(sys.argv, "--")
            return sys.argv[idx + 1:]  # the list after '--'
        except ValueError as e:  # '--' not in the list:
            return []

    def parse_args(self):
        return super().parse_args(args=self._get_argv_after_doubledash())


parser = ArgumentParserForBlender()
parser.add_argument(
    "-l", "--location", nargs="+", type=float, help="位置", default=[0, 0, 0]
)
parser.add_argument(
    "-s", "--scale", nargs="+", type=float, help="比例", default=[1, 1, 1]
)
parser.add_argument(
    "-r", "--rotation_euler", nargs="+", type=float, help="旋转", default=[0, 0, 0]
)
parser.add_argument(
    "-pl", "--pixel", nargs="+", type=int, help="像素分辨率", default=[0, 0]
)
parser.add_argument(
    "-pd",
    "--product",
    type=str,
    help="产品",
    default="/data/blender/product/Product1.glb",
)
parser.add_argument("-of", "--output_format", type=str, default="jpeg", help="输出格式")
parser.add_argument(
    "-co", "--camera_option", type=json.loads, help="镜头camera 调整", default=[]
)
parser.add_argument(
    "-mo", "--material_option", type=json.loads, help="材质material 调整", default=[]
)
try:
    args = parser.parse_args()
    old_location = tuple(args.location)
    old_scale = tuple(args.scale)
    old_rotation_euler = tuple(args.rotation_euler)
    pixel = tuple(args.pixel)

    # blender three.js 轴方向适配
    location = (old_location[0], -old_location[2], old_location[1])
    scale = (old_scale[0], old_scale[2], old_scale[1])
    rotation_euler = (old_rotation_euler[0], -old_rotation_euler[2], old_rotation_euler[1])

    camera_option = args.camera_option

    for i in camera_option:
        temp_l = tuple(i["location"])
        i['location'] = (float(temp_l[0]), -float(temp_l[2]), float(temp_l[1]))
        # temp_r = tuple(i["rotate"])
        # i["rotate"] = (float(temp_r[0]), -float(temp_r[2]), float(temp_r[1]))

    material_option = args.material_option

    of = args.output_format
    product = args.product
    add_product(product)
    update_transform(location, scale, rotation_euler)
    update_camera(camera_option)
    update_material(material_option)
    update_output(of, pixel)
except Exception as e:
    line = e.__traceback__.tb_lineno
    print('python 脚本异常 行号 {} 异常消息 {}'.format(line, str(e)))
    sys.exit(1)
'''
import bpy
import math


def get_frame_camera(frame):
    """
    获取帧绑定的相机标记
    """
    all_markers = bpy.context.scene.timeline_markers
    for i in all_markers:
        if i.frame == frame:
            return i.camera
        
camera_option = [{"name":"default","fov":54.43222611864906,"near":0.10000000149011612,"far":100,"location":["-5.81","2.34","-1.10"],"rotate":["-2.01","-1.15","-2.05"]},{"name":"Camera001_Orientation","fov":41.11209023703316,"near":0.10000000149011612,"far":1000,"location":["-6.73","2.29","7.38"],"rotate":["1.57","-0.01","0.65"]},{"name":"Camera002_Orientation","fov":39.597755335771296,"near":0.10000000149011612,"far":1000,"location":["6.44","3.90","9.29"],"rotate":["1.45","0.06","-0.52"]}]

for i in range(len(camera_option)):
    try:
        # camera = get_frame_camera(camera_option[i]['frame'])
        camera = get_frame_camera(i + 1)
        # camera = bpy.data.cameras[camera_option[i]["name"]]
    except:
        continue
    if camera:
        temp_l = tuple(camera_option[i]['location'])
        temp_r = tuple(camera_option[i]['rotation'])
        location = (float(temp_l[0]), -float(temp_l[2]), float(temp_l[1]))
        rotation_euler = (float(temp_r[0]), -float(temp_r[2]), float(temp_r[1])) 
        camera.name = camera_option[i]["name"]
        camera.data.sensor_height = 50  # 传感器 适配尺寸 mm 高度
        camera.data.sensor_fit = "VERTICAL"  # 传感器适配方式 垂直
        camera.data.lens_unit = 'FOV' # 镜头单位  焦距
        camera.data.angle = math.radians(float(camera_option[i]["fov"]))
        camera.data.clip_start = float(camera_option[i]["near"])
        camera.data.clip_end = float(camera_option[i]["far"])
        camera.location = location
        camera.rotation_mode = "YZX"
        camera.rotation_euler = rotation_euler
'''
#
# test = {
#     "location": "0.02,0.40,-0.23",
#     "scale": "0.81,0.81,0.81",
#     "rotate": "0,0,0",
#     "cameraOption": [
#         {
#             "name": "Picture003",
#             "fov": "22.90",
#             "near": "0.10",
#             "far": "1000.00",
#             "location": [
#                 "10.17",
#                 "7.01",
#                 "13.81"
#             ],
#             "rotation": [
#                 "1.50",
#                 "0.05",
#                 "-0.63"
#             ]
#         }
#     ]
# }

#
# import bpy
# camera = bpy.data.objects[test['cameraOption']['name']]
# camera.data.sensor_height = 50  # 传感器 适配尺寸 mm 高度
# camera.data.sensor_fit = "VERTICAL"  # 传感器适配方式 垂直
# camera.data.lens_unit = 'FOV'  # 镜头单位  焦距
# camera.data.angle = math.radians(float(test['cameraOption'][0]["fov"]))
# camera.data.clip_start = float(test['cameraOption'][0]["near"])
# camera.data.clip_end = float(test['cameraOption'][0]["far"])
# temp_l = tuple(test['cameraOption'][0]["location"])
# camera.location = (float(temp_l[0]), -float(temp_l[2]), float(temp_l[1]))
# temp_r = tuple(test['cameraOption'][0]["rotation"])
# camera.rotation_mode = "YZX"
# camera.rotation_euler = (float(temp_r[0]), -float(temp_r[2]), float(temp_r[1]))
