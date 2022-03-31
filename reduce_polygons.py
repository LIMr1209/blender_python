import bpy

ex_path = r'C:\Users\thn\Desktop\test.glb'
obj = bpy.data.objects['猴头']
decimate = obj.modifiers.new(name='DECIMATE', type='DECIMATE')  # 新建精简修改器
decimate.ratio = 0.5  # 比率
# 应用修改器导出glb
bpy.ops.export_scene.gltf(filepath=ex_path, export_colors=True, export_draco_mesh_compression_enable=True,
                              export_cameras=False, use_selection=True, use_visible=False, export_apply=True,
                              export_lights=False, export_selected=True, export_image_format='JPEG')
