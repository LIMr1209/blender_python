import bpy

map = r'C:\Users\thn\Downloads\094_hdrmaps_com_free.exr'
bpy.context.scene.world.use_nodes = True
nodes = bpy.context.scene.world.node_tree.nodes
links = bpy.context.scene.world.node_tree.links
background = nodes.get('Background')
environment_image_node = nodes.new(type='ShaderNodeTexEnvironment')
environment_image_node.label = "EnvironmentIMG"
environment_image_node.name = "EnvironmentIMG"
links.new(environment_image_node.outputs['Color'], background.inputs['Color'])
environment_image_node.image = bpy.data.images.load(map)
