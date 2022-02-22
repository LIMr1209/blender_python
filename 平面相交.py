import bpy
import mathutils
from bpy_extras.object_utils import object_data_add


def objects_return(obj):
    mat = obj.matrix_world
    v0 = mat @ obj.data.vertices[0].co
    v1 = mat @ obj.data.vertices[1].co
    v2 = mat @ obj.data.vertices[2].co
    normal = mathutils.geometry.normal(v0, v1, v2)
    r = [v0, normal]
    return r


def new_object(verts):
    mesh = bpy.data.meshes.new(name="new line")
    mesh.from_pydata(verts, [], [])
    object_data_add(bpy.context, mesh, operator=None)


print("#" * 15)
p1 = bpy.data.objects['Plane']
p2 = bpy.data.objects['Plane.001']

a = objects_return(p1)
b = objects_return(p2)

c = mathutils.geometry.intersect_plane_plane(a[0], a[1], b[0], b[1])

bpy.context.scene.cursor.location = c[0]
vertices = [tuple(c[0]), tuple(c[1])]
edges = [tuple(c[0]), tuple(c[1])]

new_object(vertices)
