import bpy
import math
import re


def standard():
    try:
        bpy.data.materials['StandardMaterial']
    except:
        standard_material()


def standard_material():
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

    mat_output_node = nodes.get('Material Output')
    mat_output_node.label = 'matOutput'
    mat_output_node.name = 'matOutput'


def rename_scene_object():
    """
    ?????????????????? ???????????? ??????????????????????????????????????????
    """
    objs = bpy.data.objects[:]
    for i in objs:
        i.name = 'scene.' + i.name


def get_frame_camera(frame):
    """
    ??????????????????????????????
    """
    all_markers = bpy.context.scene.timeline_markers
    for i in all_markers:
        if i.frame == frame:
            return i.camera


def remove_empty():
    """
    ???????????????
    """
    while True:
        model = bpy.context.selected_objects[:]
        # ???????????????
        objs = [
            i
            for i in model
            if i.type in ["EMPTY", "LIGHT", "CAMERA"] and not i.children
        ]
        bpy.ops.object.delete({"selected_objects": objs})
        if not objs:
            break


def add_product(model_path):
    """
    ??????????????????
    :param model_path: ??????????????????
    :return:
    """

    bpy.ops.import_scene.gltf(filepath=model_path)

    # ???????????????
    remove_empty()
    # ??????
    model = bpy.context.selected_objects[:]
    for i in model:
        if i.type != "EMPTY":
            i.name = "soul_product"
            bpy.context.view_layer.objects.active = i
            break
    bpy.ops.object.join()
    # ???????????????
    remove_empty()
    # ????????????
    bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
    # ????????????
    model = bpy.context.selected_objects[:]
    for i in model:
        i.animation_data_clear()

    name_index = 0
    while True:
        pd = bpy.data.objects['soul_product']
        parent = pd.parent
        if parent:
            name_index += 1
            pd.name = 'soul_product.' + str(name_index).zfill(4)
            parent.name = 'soul_product'
        else:
            break
    # ????????????????????? ?????????????????? ??????
    bpy.ops.object.empty_add(
        type="PLAIN_AXES", align="WORLD", location=(0, 0, 0), scale=(1, 1, 1)
    )
    bpy.context.object.name = "ProductContainer"
    pd = bpy.data.objects["soul_product"]
    pdc = bpy.data.objects["ProductContainer"]
    pd.parent = pdc


def add_product_new(model_path):
    """
    ??????????????????
    :param model_path: ??????????????????
    :return:
    """
    # rename_scene_object()
    if model_path.endswith('.glb') or model_path.endswith('.gltf'):
        # file_kind = 'glb'
        bpy.ops.import_scene.gltf(filepath=model_path)
    elif model_path.endswith('.obj'):
        # file_kind = 'obj'
        bpy.ops.import_scene.obj(filepath=model_path)
    else:
        raise Exception("??????????????????????????????")
    # ???????????????
    remove_empty()
    # ????????????
    model = bpy.context.selected_objects[:]
    rex = re.compile('\.\d+$')
    for i in model:
        # if file_kind == 'glb':
        # ???????????????
        old_name = i.name
        group = rex.search(old_name)
        if group:
            index = group.span()[0]
            new_name = old_name[:index] + old_name[index + 1:]
            i.name = new_name
        i.name = i.name.replace(' - ', '_-_')
        # ????????????
        i.animation_data_clear()
    # ????????????????????? ?????????????????? ??????
    bpy.ops.object.empty_add(
        type="PLAIN_AXES", align="WORLD", location=(0, 0, 0), scale=(1, 1, 1)
    )
    bpy.context.object.name = "ProductContainer"
    pdc = bpy.data.objects["ProductContainer"]
    for i in model:
        if not i.parent:
            i.parent = pdc

    # ??????????????? ?????? three js ????????????
    # if file_kind == 'glb':
    for i in model:
        if i.type == 'MESH':
            bpy.ops.object.select_all(action='DESELECT')
            i.select_set(True)
            bpy.context.view_layer.objects.active = i
            old_name = i.name
            bpy.ops.mesh.separate(type="MATERIAL")  # ???????????????
            separate_models = bpy.context.selected_objects[:]
            separate_models = list(reversed(separate_models))
            if len(separate_models) > 1:
                for z, y in enumerate(separate_models):
                    y.name = old_name + "_%s" % str(z + 1)


def update_disable(disable):
    """
    ????????????
    :param disable: ?????????????????????
    :return:
    """
    for i in disable:
        obj = bpy.data.objects[i]
        obj.hide_render = True


def update_transform(location, scale, rotation_euler):
    """
    ??????????????????
    :param location: ??????
    :param scale: ????????????
    :param rotation_euler: ????????????
    :return:
    """
    pd = bpy.data.objects["ProductContainer"]
    pd.location = location  # ????????????
    pd.scale = scale  # ??????????????????
    pd.rotation_mode = "YZX"  # ????????????
    pd.rotation_euler = rotation_euler  # ??????????????????


def update_camera(camera_option):
    """
    ?????????????????????
    :param camera_option: ????????????
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
            camera.data.sensor_height = 50  # ????????? ???????????? mm ??????
            camera.data.sensor_fit = "VERTICAL"  # ????????????????????? ??????
            camera.data.lens_unit = 'FOV'  # ????????????  ??????
            camera.data.angle = math.radians(float(camera_option[i]["fov"]))
            camera.data.clip_start = float(camera_option[i]["near"])
            camera.data.clip_end = float(camera_option[i]["far"])
            camera.location = camera_option[i]["location"]
            # ???????????????  ?????????????????????
            # camera.rotation_mode = "YZX"
            # YXZ
            # camera.rotation_euler = camera_option[i]["rotate"]
            # ?????????????????????  ???????????????????????????
            # rotate = camera_option[i]["rotate"]
            # m = Euler((float(rotate[0]), float(rotate[1]), float(rotate[2])),
            #           'ZYX').to_matrix()
            # b_m = [m[0], -m[2], m[1]]
            # matrix = Matrix(b_m)
            # euler = matrix.to_euler('XYZ')
            # camera.rotation_mode = "XYZ"
            # camera.rotation_euler = euler
            # ????????? ????????????
            # "x":(tmp_rotation.x*180/Math.PI + 90).toFixed(3),
            # "y":(tmp_rotation.z*180/Math.PI).toFixed(3),
            # "z":(tmp_rotation.y*180/Math.PI).toFixed(3)
            camera.rotation_mode = "YXZ"
            camera.rotation_euler = camera_option[i]["rotate"]


## HEX???linearRGB
def srgb_to_linearrgb(c):
    if c < 0:
        return 0
    elif c < 0.04045:
        return c / 12.92
    else:
        return ((c + 0.055) / 1.055) ** 2.4


def hex2rgb(color, alpha=1):
    color = int('0x' + color[1:], 16)  # #FFFFFF
    r = (color & 0xff0000) >> 16
    g = (color & 0x00ff00) >> 8
    b = (color & 0x0000ff)
    return tuple([srgb_to_linearrgb(c / 0xff) for c in (r, g, b)] + [alpha])


# ?????????
def Basecolor(color, map, baseColorIMG, baseColorRGB, baseColorMix, links, BSDF):
    if map:
        baseColorIMG.image = bpy.data.images.load(map)
        baseColorRGB.outputs[0].default_value = (hex2rgb(color))
        links.new(baseColorMix.outputs[0], BSDF.inputs['Base Color'])
    else:
        baseColorRGB.outputs[0].default_value = (hex2rgb(color))
        links.new(baseColorRGB.outputs[0], BSDF.inputs['Base Color'])


# ?????????
def Metallic(metalness, metalnessMap, metallicIMG, metallicFactor, metallicMix, links, BSDF):
    if metalnessMap:
        metallicIMG.image = bpy.data.images.load(metalnessMap)
        metallicIMG.image.colorspace_settings.name = 'Non-Color'
        metallicFactor.outputs[0].default_value = 1
        links.new(metallicMix.outputs[0], BSDF.inputs['Metallic'])
    else:
        metallicFactor.outputs[0].default_value = metalness
        links.new(metallicFactor.outputs[0], BSDF.inputs['Metallic'])


# ?????????
def Roughness(roughness, roughnessMap, roughnessIMG, roughnessFactor, roughnessMix, links, BSDF):
    if roughnessMap:
        roughnessIMG.image = bpy.data.images.load(roughnessMap)
        roughnessIMG.image.colorspace_settings.name = 'Non-Color'
        roughnessFactor.outputs[0].default_value = 1
        links.new(roughnessMix.outputs[0], BSDF.inputs['Roughness'])
    else:
        roughnessFactor.outputs[0].default_value = roughness
        links.new(roughnessFactor.outputs[0], BSDF.inputs['Roughness'])


# ?????????
# def Transmission(ior, transmission, iorFactor, transmissionFactor, links, BSDF):
#     iorFactor.outputs[0].default_value = ior
#     transmissionFactor.outputs[0].default_value = transmission
#     links.new(iorFactor.outputs[0], BSDF.inputs[14])
#     links.new(transmissionFactor.outputs[0], BSDF.inputs[15])

# ?????????
def Transmission(ior, transmission, iorFactor, transmissionFactor, transMix, matOutput, links, BSDF):
    iorFactor.outputs[0].default_value = ior
    transmissionFactor.outputs[0].default_value = transmission
    links.new(iorFactor.outputs[0], BSDF.inputs['IOR'])
    links.new(transmissionFactor.outputs[0], BSDF.inputs['Transmission'])
    if transmission != 0:
        links.new(BSDF.outputs[0], transMix.inputs[1])
        links.new(transMix.outputs[0], matOutput.inputs[0])


# ??????
def Emission(emissive, emissiveIntensity, emissiveMap, emissiveIMG, emissiveRGB, emissiveFactor, emissiveMix, links,
             BSDF):
    if emissiveMap:
        emissiveIMG.image = bpy.data.images.load(emissiveMap)
        emissiveRGB.outputs[0].default_value = (1, 1, 1, 1)
        emissiveFactor.outputs[0].default_value = emissiveIntensity
        links.new(emissiveMix.outputs[0], BSDF.inputs['Emission'])
        links.new(emissiveFactor.outputs[0], BSDF.inputs['Emission Strength'])
    else:
        emissiveRGB.outputs[0].default_value = (hex2rgb(emissive))
        emissiveFactor.outputs[0].default_value = emissiveIntensity
        links.new(emissiveRGB.outputs[0], BSDF.inputs['Emission'])
        links.new(emissiveFactor.outputs[0], BSDF.inputs['Emission Strength'])


# ??????/??????
def Normal(normalMap, NormalMap, normalIMG, links, BSDF):
    if normalMap:
        normalIMG.image = bpy.data.images.load(normalMap)
        normalIMG.image.colorspace_settings.name = 'Non-Color'
        links.new(NormalMap.outputs[0], BSDF.inputs['Normal'])


def update_material(material_option):
    """
    ??????????????????
    :param material_option: ????????????
    :return:
    """
    # for j, i in enumerate(material_option):
    for i in material_option:
        mat_template = bpy.data.materials['StandardMaterial']
        name = i['name']
        try:
            obj = bpy.data.objects[name]
        except:
            try:
                new_name = name.capitalize()
                obj = bpy.data.objects[new_name]
            except:
                continue
        mat = mat_template.copy()
        obj.active_material = mat
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links
        BSDF = nodes.get('Principled BSDF')
        baseColorIMG = nodes.get('baseColorIMG')
        baseColorRGB = nodes.get('baseColorRGB')
        baseColorMix = nodes.get('baseColorMix')
        metallicMix = nodes.get('metallicMix')
        metallicIMG = nodes.get('metallicIMG')
        metallicFactor = nodes.get('metallicFactor')
        roughnessIMG = nodes.get('roughnessIMG')
        roughnessFactor = nodes.get('roughnessFactor')
        roughnessMix = nodes.get('roughnessMix')
        iorFactor = nodes.get('iorFactor')
        transmissionFactor = nodes.get('transmissionFactor')
        emissiveIMG = nodes.get('emissiveIMG')
        emissiveRGB = nodes.get('emissiveRGB')
        emissiveMix = nodes.get('emissiveMix')
        emissiveFactor = nodes.get('emissiveFactor')
        normalIMG = nodes.get('normalIMG')
        normalFactor = nodes.get('normalFactor')
        NormalMap = nodes.get('NormalMap')
        transBSDF = nodes.get('transBSDF')
        transMix = nodes.get('transMix')
        matOutput = nodes.get('matOutput')
        color = i.get('color')
        map = i.get('map')
        metalness = i.get('metalness', 0)
        metalnessMap = i.get('metalnessMap')
        roughness = i.get('roughness', 0)
        roughnessMap = i.get('roughnessMap')
        ior = i.get('ior', 0)
        transmission = i.get('transmission', 0)
        emissive = i.get('emissive', '#000000')
        emissiveIntensity = i.get('emissiveIntensity', 0)
        emissiveMap = i.get('emissiveMap')
        normalMap = i.get('normalMap')
        Basecolor(color, map, baseColorIMG, baseColorRGB, baseColorMix, links, BSDF)
        Metallic(metalness, metalnessMap, metallicIMG, metallicFactor, metallicMix, links, BSDF)
        Roughness(roughness, roughnessMap, roughnessIMG, roughnessFactor, roughnessMix, links, BSDF)
        Transmission(ior, transmission, iorFactor, transmissionFactor, transMix, matOutput, links, BSDF)
        Emission(emissive, emissiveIntensity, emissiveMap, emissiveIMG, emissiveRGB, emissiveFactor, emissiveMix, links,
                 BSDF)
        Normal(normalMap, NormalMap, normalIMG, links, BSDF)


material_option = [
    {'name': 'cgaxis_modela_116_17_10_01', 'color': '#2CBC0F',
     'map': r'C:\Users\thn\Desktop\soul_data\material\marble_016\Color.jpg'},
    {'name': 'cup_001001', 'color': '#BC252F', 'map': r'C:\Users\thn\Desktop\soul_data\material\candy_001\Color.jpg'}
]
product_option = [
    {'file_path': r'C:\Users\thn\Desktop\soul_data\element\6239a46e67144e33686aadba.glb',
     'location': [-2.409, 6.175, 6.693],
     'scale': [2, 2, 2], 'rotate': [-91.81, -33.41, -93.08]},
    {'file_path': r'C:\Users\thn\Desktop\soul_data\element\6239a4c067144e33686aadc9.glb',
     'location': [4.324, 6.573, 4.813],
     'scale': [1, 1, 1], 'rotate': [56.59, -27.88, 72.85]},
]
standard()
for d in product_option:
    add_product_new(d['file_path'])
    location = (d['location'][0], -d['location'][2], d['location'][1])
    scale = (d['scale'][0], d['scale'][2], d['scale'][1])
    rotation_euler = (d['rotate'][0], -d['rotate'][2], d['rotate'][1])
    # rotation_euler = (math.radians(d['rotate'][0]), -math.radians(d['rotate'][2]), math.radians(d['rotate'][1]))
    update_transform(location, scale, rotation_euler)
update_material(material_option)
