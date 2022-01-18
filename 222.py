import bpy
from mathutils import Vector
from functools import reduce
from itertools import product


def merge_boxes(objects):
    return reduce(lambda x, y: x + y,
                  [Box(obj) for obj in objects if obj.type == 'MESH'])


class Box:
    def __init__(self, bl_object=None, max_min=None):
        if bl_object and bl_object.type == 'MESH':
            self.__bound_box = self.__get_bound_box_from_object(bl_object)
        elif max_min:
            self.__bound_box = self.__get_bound_box_from_max_min(max_min)
        else:
            raise TypeError()

    def __add__(self, bound_box):
        return self.merge(bound_box)

    def __getitem__(self, index):
        return self.__bound_box[index]

    @property
    def max(self):
        return Vector(max((v.x, v.y, v.z) for v in self.__bound_box))

    @property
    def min(self):
        return Vector(min((v.x, v.y, v.z) for v in self.__bound_box))

    @property
    def center(self):
        return sum((v for v in self.__bound_box), Vector()) / 8

    def merge(self, box):
        if not box:
            return self
        if not isinstance(box, Box):
            raise TypeError('Require a Box object')
        max_new = Vector(map(max, zip(self.max, box.max)))
        min_new = Vector(map(min, zip(self.min, box.min)))
        return Box(max_min=(max_new, min_new))

    def __get_bound_box_from_object(self, bl_object):
        return [bl_object.matrix_world @ Vector(v) for v in bl_object.bound_box]

    def __get_bound_box_from_max_min(self, max_min):
        max_point, min_point = max_min
        return [Vector(v) for v in
                product((max_point.x, min_point.x), (max_point.y, min_point.y), (max_point.z, min_point.z))]


if __name__ == '__main__':
    box1 = Box(bpy.context.object)
    print("Box1 Center: %s" % box1.center)
    print("Box1 max: %s" % box1.max)
    print("Box1 min: %s" % box1.min)

    box2 = merge_boxes(bpy.data.objects)
    print("Box2 Center: %s" % box2.center)
    print("Box2 max: %s" % box2.max)
    print("Box2 min: %s" % box2.min)
