import bpy

mat = bpy.data.materials.new("StandardMaterial")
mat.use_nodes = True
nodes = mat.node_tree.nodes
links = mat.node_tree.links

bsdf_node = nodes['Principled BSDF']
text_coord_node = nodes.new(type='ShaderNodeTexCoord')
mapping_node = nodes.new(type="ShaderNodeMapping")
links.new(text_coord_node.outputs['UV'], mapping_node.inputs['Vector'])

base_color_img_node = nodes.new(type='ShaderNodeTexImage')
base_color_img_node.label = "baseColorIMG"
base_color_img_node.name = "baseColorIMG"
links.new(mapping_node.outputs['Vector'], base_color_img_node.inputs['Vector'])
base_color_mix_rgb_node = nodes.new(type="ShaderNodeMixRGB")
base_color_mix_rgb_node.blend_type = 'MULTIPLY'
base_color_mix_rgb_node.label = 'baseColorMix'
base_color_mix_rgb_node.name = 'baseColorMix'
base_color_mix_rgb_node.inputs['Fac'].default_value = 1
base_color_rgb_node = nodes.new(type="ShaderNodeRGB")
base_color_rgb_node.label = 'baseColorRGB'
base_color_rgb_node.name = 'baseColorRGB'
links.new(base_color_img_node.outputs['Color'], base_color_mix_rgb_node.inputs['Color1'])
links.new(base_color_rgb_node.outputs['Color'], base_color_mix_rgb_node.inputs['Color2'])
links.new(base_color_rgb_node.outputs['Color'], bsdf_node.inputs['Base Color'])

metallic_img_node = nodes.new(type='ShaderNodeTexImage')
metallic_img_node.label = "metallicIMG"
metallic_img_node.name = "metallicIMG"
links.new(mapping_node.outputs['Vector'], metallic_img_node.inputs['Vector'])
metallic_separate_rgb_node = nodes.new(type='ShaderNodeSeparateRGB')
metallic_separate_rgb_node.label = 'metallicSeparateRGB'
metallic_separate_rgb_node.name = 'metallicSeparateRGB'
links.new(metallic_img_node.outputs['Color'], metallic_separate_rgb_node.inputs['Image'])
metallic_mix_node = nodes.new(type='ShaderNodeMath')
metallic_mix_node.label = 'metallicMix'
metallic_mix_node.name = 'metallicMix'
metallic_mix_node.operation = 'MULTIPLY'
links.new(metallic_separate_rgb_node.outputs['B'], metallic_mix_node.inputs[0])
metallic_factor_node = nodes.new(type='ShaderNodeValue')
metallic_factor_node.label = 'metallicFactor'
metallic_factor_node.name = 'metallicFactor'
links.new(metallic_factor_node.outputs['Value'], metallic_mix_node.inputs[1])
links.new(metallic_factor_node.outputs['Value'], bsdf_node.inputs['Metallic'])

roughness_img_node = nodes.new(type='ShaderNodeTexImage')
roughness_img_node.label = "roughnessIMG"
roughness_img_node.name = "roughnessIMG"
links.new(mapping_node.outputs['Vector'], roughness_img_node.inputs['Vector'])
roughness_separate_rgb_node = nodes.new(type='ShaderNodeSeparateRGB')
roughness_separate_rgb_node.label = 'roughnessSeparateRGB'
roughness_separate_rgb_node.name = 'roughnessSeparateRGB'
links.new(roughness_img_node.outputs['Color'], roughness_separate_rgb_node.inputs['Image'])
roughness_mix_node = nodes.new(type='ShaderNodeMath')
roughness_mix_node.label = 'roughnessMix'
roughness_mix_node.name = 'roughnessMix'
roughness_mix_node.operation = 'MULTIPLY'
links.new(roughness_separate_rgb_node.outputs['B'], roughness_mix_node.inputs[0])
roughness_factor_node = nodes.new(type='ShaderNodeValue')
roughness_factor_node.label = 'roughnessFactor'
roughness_factor_node.name = 'roughnessFactor'
roughness_factor_node.outputs['Value'].default_value = 0.5
links.new(roughness_factor_node.outputs['Value'], roughness_mix_node.inputs[1])
links.new(roughness_factor_node.outputs['Value'], bsdf_node.inputs['Roughness'])

ior_factor_node = nodes.new(type='ShaderNodeValue')
ior_factor_node.label = 'iorFactor'
ior_factor_node.name = 'iorFactor'
ior_factor_node.outputs['Value'].default_value = 1.450
links.new(ior_factor_node.outputs['Value'], bsdf_node.inputs['IOR'])
transmission_factor_node = nodes.new(type='ShaderNodeValue')
transmission_factor_node.label = 'transmissionFactor'
transmission_factor_node.name = 'transmissionFactor'
links.new(transmission_factor_node.outputs['Value'], bsdf_node.inputs['Transmission'])
trans_bsdf_node = nodes.new(type="ShaderNodeBsdfTransparent")
trans_bsdf_node.label = 'transBSDF'
trans_bsdf_node.name = 'transBSDF'
trans_mix_node = nodes.new(type="ShaderNodeMixShader")
trans_mix_node.label = 'transMix'
trans_mix_node.name = 'transMix'
trans_mix_node.inputs['Fac'].default_value = 0.75
links.new(trans_bsdf_node.outputs['BSDF'], trans_mix_node.inputs[2])

emissive_img_node = nodes.new(type='ShaderNodeTexImage')
emissive_img_node.label = "emissiveIMG"
emissive_img_node.name = "emissiveIMG"
links.new(mapping_node.outputs['Vector'], emissive_img_node.inputs['Vector'])
emissive_mix_rgb_node = nodes.new(type="ShaderNodeMixRGB")
emissive_mix_rgb_node.blend_type = 'MULTIPLY'
emissive_mix_rgb_node.label = 'emissiveMix'
emissive_mix_rgb_node.name = 'emissiveMix'
emissive_mix_rgb_node.inputs['Fac'].default_value = 1
emissive_rgb_node = nodes.new(type="ShaderNodeRGB")
emissive_rgb_node.label = 'emissiveRGB'
emissive_rgb_node.name = 'emissiveRGB'
links.new(emissive_img_node.outputs['Color'], emissive_mix_rgb_node.inputs['Color1'])
links.new(emissive_rgb_node.outputs['Color'], emissive_mix_rgb_node.inputs['Color2'])
links.new(emissive_rgb_node.outputs['Color'], bsdf_node.inputs['Emission'])
emissive_factor_node = nodes.new(type='ShaderNodeValue')
emissive_factor_node.label = 'emissiveFactor'
emissive_factor_node.name = 'emissiveFactor'
emissive_factor_node.outputs['Value'].default_value = 1
links.new(emissive_factor_node.outputs['Value'], bsdf_node.inputs['Emission Strength'])

normal_img_node = nodes.new(type='ShaderNodeTexImage')
normal_img_node.label = "normalIMG"
normal_img_node.name = "normalIMG"
links.new(mapping_node.outputs['Vector'], normal_img_node.inputs['Vector'])
normal_factor_node = nodes.new(type='ShaderNodeValue')
normal_factor_node.label = 'normalFactor'
normal_factor_node.name = 'normalFactor'
normal_factor_node.outputs['Value'].default_value = 0.5
normal_map_node = nodes.new(type='ShaderNodeNormalMap')
normal_map_node.label = 'NormalMap'
normal_map_node.name = 'NormalMap'
normal_map_node.uv_map = 'UVMap'
links.new(normal_factor_node.outputs['Value'], normal_map_node.inputs['Strength'])
links.new(normal_img_node.outputs['Color'], normal_map_node.inputs['Color'])
