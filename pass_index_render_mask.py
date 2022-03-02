import bpy

# 物体索引渲染遮罩 mask 图 用作元素模型封面图 换底色
obj_name = 'Cube'
pass_index = 1
output_file_path = r'C:\Users\thn\Desktop'
scene = bpy.context.scene
scene.render.engine = 'CYCLES'  # 启用 CYCLES 渲染引擎
scene.view_layers['ViewLayer'].use_pass_object_index = True  # 打开试图层物体索引通道
bpy.data.objects[obj_name].pass_index = pass_index  # 设置物体索引通道

scene.use_nodes = True  # 场景使用节点
nodes = scene.node_tree.nodes
links = scene.node_tree.links
render_layers_node = nodes['Render Layers']
id_mask_node = nodes.new(type='CompositorNodeIDMask')
id_mask_node.index = pass_index  # 设置节点索引通道
id_mask_node.use_antialiasing = True  # 抗锯齿
links.new(render_layers_node.outputs['IndexOB'], id_mask_node.inputs['ID value'])
output_file_node = nodes.new(type='CompositorNodeOutputFile')
output_file_node.base_path = output_file_path
output_file_node.file_slots['Image'].path = 'mask'
links.new(id_mask_node.outputs['Alpha'], output_file_node.inputs['Image'])
