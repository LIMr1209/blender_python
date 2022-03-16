# glb 保留变换信息，格式化为两层结构
def export_gltf(output_file):
    model = bpy.context.selected_objects[:]
    rex = re.compile('\.\d+$')
    for i in model:
        # if file_kind == 'glb':
        # 去除小数点
        old_name = i.name
        group = rex.search(old_name)
        if group:
            index = group.span()[0]
            new_name = old_name[:index] + old_name[index + 1:]
            i.name = new_name
        i.name = i.name.replace(' - ', '_-_')
    # ex_path = data_path + '/uma/' + os.path.splitext(item)[0] + '_uma.glb'
    ex_path = output_file
    bpy.ops.export_scene.gltf(filepath=ex_path, export_colors=False, export_draco_mesh_compression_enable=True,
                              export_cameras=True, use_selection=True, use_visible=False, export_apply=True,
                              export_lights=True)
    return {'FINISHED'}


import re
import bpy
from mathutils import Vector


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


def clearObjects():
    try:
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete()
    except:
        pass


def clearCollections():
    try:
        for c in bpy.context.scene.collection.children:
            bpy.context.scene.collection.children.unlink(c)
        for c in bpy.data.collections:
            if not c.users:
                bpy.data.collections.remove(c)
    except:
        pass


clearObjects()
clearCollections()

collection = bpy.data.collections.new('Protect')
bpy.context.scene.collection.children.link(collection)

collection = bpy.data.collections.new('Origin')
bpy.context.scene.collection.children.link(collection)

collection = bpy.data.collections.new('Join')
bpy.context.scene.collection.children.link(collection)

protect = bpy.data.collections['Protect']
originPd = bpy.data.collections['Origin']
joinPd = bpy.data.collections['Join']

protect.color_tag = 'COLOR_01'
originPd.color_tag = 'COLOR_02'
joinPd.color_tag = 'COLOR_03'

input_file = r'C:\Users\thn\Desktop\coffee_maker_001.glb'
layer_collection = bpy.context.view_layer.layer_collection
bpy.context.view_layer.active_layer_collection = layer_collection

if input_file.endswith('.glb') or input_file.endswith('.gltf'):
    bpy.ops.import_scene.gltf(filepath=input_file)

if input_file.endswith('.fbx'):
    bpy.ops.import_scene.fbx(filepath=input_file)

if input_file.endswith('.obj'):
    bpy.ops.import_scene.obj(filepath=input_file)

bpy.ops.object.make_single_user(object=True, obdata=True, material=True)
bpy.ops.object.transform_apply(location=True, rotation=True, scale=True)
# bpy.ops.object.transform_apply(location=True, rotation=True)
selected_objects = bpy.context.selected_objects

for o in selected_objects:
    bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
    bpy.context.scene.collection.objects.unlink(o)
    originPd.objects.link(o)

remove_empty()

for o in originPd.objects:
    if o.type == 'MESH' and o.hide_select == False:
        od = o.copy()
        od.data = o.data.copy()
        joinPd.objects.link(od)

# join
bpy.ops.object.select_all(action='DESELECT')
for o in joinPd.objects:
    if o.type == 'MESH':
        o.select_set(True)
        bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
        bpy.context.view_layer.objects.active = o

bpy.ops.object.join()

# rename join object and mesh
for o in joinPd.objects:
    o.name = "product2trans"

for o in originPd.objects:
    if o.type == 'MESH':
        o.name = o.data.name

i = 0
for o in originPd.objects:
    if o.type == 'MESH':
        o.name = "部件." + str(i)
        o.data.name = o.name
        o.data.name = "uma_Mesh." + str(i)
    i += 1

pd = bpy.data.objects['product2trans']
dimensions = pd.dimensions
scale = pd.scale
# bpy.data.objects.remove(pd)
# 设定父级，并保留变换
bpy.ops.object.empty_add(type='PLAIN_AXES', align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.context.object.name = "ProductContainer"
pdc = bpy.data.objects['ProductContainer']
for o in originPd.objects:
    if o.parent == None:
        o.select_set(True)

bpy.context.view_layer.objects.active = pdc
bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
bpy.ops.object.select_all(action='DESELECT')

pd_box = [pd.matrix_world @ Vector(pdBvert) for pdBvert in pd.bound_box]
x = (pd_box[0][0] + pd_box[4][0]) / 2
y = (pd_box[0][1] + pd_box[2][1]) / 2
z = (pd_box[0][2] + pd_box[1][2]) / 2

for o in originPd.objects:
    o.location.x -= x - pdc.location.x
    o.location.y -= y - pdc.location.y
    o.location.z -= z - pdc.location.z

# clearObjects()
pd.select_set(True)
bpy.context.view_layer.objects.active = pd
bpy.context.scene.cursor.location = x, y, z
bpy.ops.object.origin_set(type='ORIGIN_CURSOR')
pd.location = 0, 0, 0
bpy.context.scene.cursor.location = 0, 0, 0