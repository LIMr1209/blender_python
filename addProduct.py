import argparse
import sys
import bpy
from mathutils import Vector


def add_product(model_path):
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

    bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    bpy.context.object.name = "ProductContainer"

    pdc = bpy.data.objects['ProductContainer']
    pd = bpy.data.objects['product']
    lp = bpy.data.objects['LocatedCube']
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


def add_product_old(model_path):
    """
    场景添加产品
    :param model_path: 产品模型路径
    :return:
    """

    bpy.ops.import_scene.gltf(filepath=model_path)

    model = bpy.context.selected_objects[:]
    model[0].name = 'product'
    bpy.context.view_layer.objects.active = model[0]
    bpy.ops.object.join()
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
    # bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    # bpy.context.object.name = "ProductContainer"
    #
    # pdc = bpy.data.objects['ProductContainer']
    # pd = bpy.data.objects['product']
    # pd.parent = pdc


def update_transform(location, scale, rotation_euler):
    """
    更新变换信息
    :param location: 位置
    :param scale: 大小比例
    :param rotation_euler: 欧拉旋转
    :return:
    """
    pd = bpy.data.objects['product']
    pd.delta_location = location  # 更新位置
    # pd.delta_scale = scale  # 更新大小比例
    pd.scale = scale  # 更新大小比例
    pd.rotation_mode = 'YZX'  # 旋转模式
    # pd.delta_rotation_euler = rotation_euler  # 更新欧拉旋转
    pd.rotation_euler = rotation_euler  # 更新欧拉旋转


def update_output(of):
    """
    更新输出选项
    :param of: jpeg 或者 mp4
    :return:
    """
    if of == 'jpeg':
        bpy.context.scene.render.image_settings.file_format = 'JPEG'
        bpy.context.scene.cycles.samples = 64
        bpy.context.scene.render.resolution_percentage = 40
    elif of == 'ffmpeg':
        bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
        bpy.context.scene.render.ffmpeg.constant_rate_factor = 'HIGH'
        bpy.context.scene.render.ffmpeg.format = 'MPEG4'
        bpy.context.scene.cycles.samples = 64
        bpy.context.scene.render.resolution_percentage = 40


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
parser.add_argument("-l", "--location", nargs="+", type=float,
                    help="位置", default=[0, 0, 0])
parser.add_argument("-s", "--scale", nargs="+", type=float,
                    help="比例", default=[1, 1, 1])
parser.add_argument("-r", "--rotation_euler", nargs="+", type=float,
                    help="旋转", default=[0, 0, 0])
parser.add_argument("-pd", "--product", type=str, help="产品", default='/data/blender/product/Product1.glb')
parser.add_argument('-of', '--output_format', type=str, default='jpeg', help='输出格式')

args = parser.parse_args()
old_location = tuple(args.location)
old_scale = tuple(args.scale)
old_rotation_euler = tuple(args.rotation_euler)

# blender three.js 轴方向适配
location = (old_location[0], -old_location[2], old_location[1])
scale = (old_scale[0], old_scale[2], old_scale[1])
rotation_euler = (old_rotation_euler[0], -old_rotation_euler[2], old_rotation_euler[1])

of = args.output_format
product = args.product
add_product_old(product)
update_transform(location, scale, rotation_euler)
update_output(of)
