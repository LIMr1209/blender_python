import bpy

# init material
mat = bpy.data.materials["StandardMaterial"]

data = {"name": "默认值.059", "color": "#ffffff", "map": "", "metalness": 0.0, "metalnessMap": "", "roughness": 0.2, "roughnessMap": "", "emissive": "#000000", "emissiveMap": "", "emissiveIntensity": 1.0, "normalMap": "", "transmission": 1.0, "ior": 2.0}

objName = data.get('name')
color = data.get('color')
map = data.get('map')
metalness = data.get('metalness')
metalnessMap = data.get('metalnessMap')
roughness = data.get('roughness')
roughnessMap = data.get('roughnessMap')
ior = data.get('ior')
transmission = data.get('transmission')
emissive = data.get('emissive')
emissiveIntensity = data.get('emissiveIntensity')
emissiveMap = data.get('emissiveMap')
normalMap = data.get('normalMap')

# 定义节点
bpy.data.objects[objName].active_material = mat.copy()
mat = bpy.data.objects[objName].active_material
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


# HEX转linearRGB
def srgb_to_linearrgb(c):
    if c < 0:
        return 0
    elif c < 0.04045:
        return c / 12.92
    else:
        return ((c + 0.055) / 1.055) ** 2.4


def hex2rgb(color, alpha=1):
    color = int('0x'+color[1:], 16)  # #FFFFFF
    r = (color & 0xff0000) >> 16
    g = (color & 0x00ff00) >> 8
    b = (color & 0x0000ff)
    return tuple([srgb_to_linearrgb(c / 0xff) for c in (r, g, b)] + [alpha])


# 基础色
def Basecolor(color, map):
    if map:
        baseColorIMG.image = bpy.data.images.load(map)
        baseColorRGB.outputs[0].default_value = (hex2rgb(color))
        links.new(baseColorMix.outputs[0], BSDF.inputs[0])
    else:
        baseColorRGB.outputs[0].default_value = (hex2rgb(color))
        links.new(baseColorRGB.outputs[0], BSDF.inputs[0])


# 金属度
def Metallic(metalness, metalnessMap):
    if metalnessMap:
        metallicIMG.image = bpy.data.images.load(metalnessMap)
        metallicIMG.image.colorspace_settings.name = 'Non-Color'
        metallicFactor.outputs[0].default_value = 1
        links.new(metallicMix.outputs[0], BSDF.inputs[4])
    else:
        metallicFactor.outputs[0].default_value = metalness
        links.new(metallicFactor.outputs[0], BSDF.inputs[4])


# 粗糙度
def Roughness(roughness, roughnessMap):
    if roughnessMap:
        roughnessIMG.image = bpy.data.images.load(roughnessMap)
        roughnessIMG.image.colorspace_settings.name = 'Non-Color'
        roughnessFactor.outputs[0].default_value = 1
        links.new(roughnessMix.outputs[0], BSDF.inputs[7])
    else:
        roughnessFactor.outputs[0].default_value = roughness
        links.new(roughnessFactor.outputs[0], BSDF.inputs[7])


# 透射率
def Transmission(ior, transmission):
    iorFactor.outputs[0].default_value = ior
    transmissionFactor.outputs[0].default_value = transmission
    links.new(iorFactor.outputs[0], BSDF.inputs[14])
    links.new(transmissionFactor.outputs[0], BSDF.inputs[15])


# 发光
def Emission(emissive, emissiveIntensity, emissiveMap):
    if emissiveMap:
        emissiveIMG.image = bpy.data.images.load(emissiveMap)
        emissiveRGB.outputs[0].default_value = (1, 1, 1, 1)
        emissiveFactor.outputs[0].default_value = emissiveIntensity
        links.new(emissiveMix.outputs[0], BSDF.inputs[17])
        links.new(emissiveFactor.outputs[0], BSDF.inputs[18])
    else:
        emissiveRGB.outputs[0].default_value = (hex2rgb(emissive))
        emissiveFactor.outputs[0].default_value = emissiveIntensity
        links.new(emissiveRGB.outputs[0], BSDF.inputs[17])
        links.new(emissiveFactor.outputs[0], BSDF.inputs[18])


# 法线/凹凸
def Normal(normalMap):
    if normalMap:
        normalIMG.image = bpy.data.images.load(normalMap)
        normalIMG.image.colorspace_settings.name = 'Non-Color'
        links.new(NormalMap.outputs[0], BSDF.inputs[20])


Basecolor(color, map)
Metallic(metalness, metalnessMap)
Roughness(roughness, roughnessMap)
Transmission(ior, transmission)
Emission(emissive, emissiveIntensity, emissiveMap)
Normal(normalMap)
