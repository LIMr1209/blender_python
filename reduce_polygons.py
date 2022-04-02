import bpy
from PIL import Image

decimate_proportion = 0.5  # 精简比例
# 规则：
# 1.面数在各个区间范围内的 精简比例各是多少
# 2.png 图片转化为 jpg 压缩比例是多少
# 3.导出为 bin + gltf + textures 外部文件引用（相对路径）

# 精简 mesh
all_obj = bpy.data.objects
for i in all_obj:
    if i.type == 'MESH':
        len(i.data.vertices)  # 顶点数
        len(i.data.edges)  # 三角面数 多边形数
        len(i.data.polygons)  # 面数
        decimate = i.modifiers.new(name='DECIMATE', type='DECIMATE')  # 新建精简修改器
        decimate.ratio = 0.1  # 比率

all_image = bpy.data.images
for i in all_image:
    if i.file_format == 'PNG':
        i.file_format = 'JPEG'
        filepath = bpy.path.abspath('//textures/{}.jpg'.format('test'))
        i.save_render(filepath)
        image = Image.open(filepath)
        image.save(filepath, quality=95)  # 压缩 不是缩小尺寸

ex_path = r'C:\Users\thn\Desktop\精简测试\精简.gltf'
# 应用修改器导出glb
# export_apply 应用修改器
# export_format  GLTF_SEPARATE gltf 分离式
# export_texture_dir 外部资源路径
# export_image_format JPEG 图片转化为 JPEG
bpy.ops.export_scene.gltf(filepath=ex_path, export_format='GLTF_SEPARATE', export_colors=True,
                          export_texture_dir='textures',
                          export_draco_mesh_compression_enable=True, export_materials='EXPORT',
                          export_cameras=True, use_selection=False, use_visible=False, export_apply=True,
                          export_lights=True, export_selected=False, export_image_format='JPEG')
