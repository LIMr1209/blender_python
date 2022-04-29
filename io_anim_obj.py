bl_info = {
    "name": "Export Obj Animation",
    "author": "Campbell Barton",
    "version": (0, 1),
    "blender": (2, 80, 0),
    "location": "File > Export > Obj Animation (.py)",
    "description": "Export Obj Animation (.py)",
    "warning": "",
    "support": 'OFFICIAL',
    "category": "Import-Export",
}

import bpy


def write_obj_animation(filepath, frame_start, frame_end, only_selected=False):
    fw = open(filepath, 'w').write

    fw("import bpy\n"
       "objs = []\n"
       "scene = bpy.context.scene\n"
       "frame = scene.frame_current - 1\n"
       "\n")

    scene = bpy.context.scene

    objs = []

    for obj in scene.objects:
        if only_selected and not obj.select_get():
            continue

        objs.append(obj)
        fw("objs.append('%s')\n\n" % obj.name)

    frame_range = range(frame_start, frame_end + 1)

    for f in frame_range:
        scene.frame_set(f)
        fw("# new frame\n")
        fw("scene.frame_set(%d + frame)\n" % f)

        for i, obj in enumerate(objs):
            fw("obj = bpy.data.objects[objs[%d]]\n" % i)

            matrix = obj.matrix_world.copy()
            fw("obj.location = %r, %r, %r\n" % matrix.to_translation()[:])
            fw("obj.scale = %r, %r, %r\n" % matrix.to_scale()[:])
            fw("obj.rotation_euler = %r, %r, %r\n" % matrix.to_euler()[:])

            fw("obj.keyframe_insert('location')\n")
            fw("obj.keyframe_insert('scale')\n")
            fw("obj.keyframe_insert('rotation_euler')\n")

            fw("\n")


from bpy.props import StringProperty, IntProperty, BoolProperty
from bpy_extras.io_utils import ExportHelper


class ObjAnimationExporter(bpy.types.Operator, ExportHelper):
    """Save a python script which re-creates cameras and markers elsewhere"""
    bl_idname = "export_animation.obj"
    bl_label = "Export Obj Animation"

    filename_ext = ".py"
    filter_glob: StringProperty(default="*.py", options={'HIDDEN'})

    frame_start: IntProperty(name="Start Frame",
                             description="Start frame for export",
                             default=1, min=1, max=300000)
    frame_end: IntProperty(name="End Frame",
                           description="End frame for export",
                           default=250, min=1, max=300000)
    only_selected: BoolProperty(name="Only Selected",
                                default=True)

    def execute(self, context):
        write_obj_animation(self.filepath, self.frame_start, self.frame_end, self.only_selected)
        return {'FINISHED'}

    def invoke(self, context, event):
        self.frame_start = context.scene.frame_start
        self.frame_end = context.scene.frame_end

        wm = context.window_manager
        wm.fileselect_add(self)
        return {'RUNNING_MODAL'}


def menu_export(self, context):
    import os
    default_path = os.path.splitext(bpy.data.filepath)[0] + ".py" if bpy.data.filepath else 'untitled'
    self.layout.operator(ObjAnimationExporter.bl_idname, text="Obj Animation (.py)").filepath = default_path


def register():
    bpy.utils.register_class(ObjAnimationExporter)
    bpy.types.TOPBAR_MT_file_export.append(menu_export)


def unregister():
    bpy.utils.unregister_class(ObjAnimationExporter)
    bpy.types.TOPBAR_MT_file_export.remove(menu_export)


if __name__ == "__main__":
    register()
