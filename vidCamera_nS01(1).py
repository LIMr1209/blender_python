import bpy
cameras = {}
scene = bpy.context.scene
frame = 0
collection = bpy.context.blend_data.collections.new(name='vidCamera')
bpy.context.collection.children.link(collection)
bpy.data.collections['vidCamera'].color_tag = 'COLOR_05'
F = bpy.data.objects['F']
bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0, 0, 1), scale=(1, 1, 1))
camSizecube = bpy.context.selected_objects[0]
camSizecube.name = 'camSizecube'
camSizecube.hide_viewport = True
camSizecube.hide_render = True
LocatedCube = bpy.data.objects['LocatedCube']

data = bpy.data.cameras.new('vidCamera01')
data.lens = 50.0
data.shift_x = 0.0
data.shift_y = 0.0
data.clip_start = 0.10000000149011612
data.clip_end = 1000.0
data.display_size = 1.0
data.dof.use_dof = True
data.dof.focus_object = F
data.dof.aperture_fstop = 1.4
obj = bpy.data.objects.new('vidCamera01', data)
obj.hide_render = False
collection.objects.link(obj)
cameras['vidCamera01'] = obj
obj.parent = camSizecube
obj.matrix_parent_inverse = camSizecube.matrix_world.inverted()

data = bpy.data.cameras.new('vidCamera02')
data.lens = 50.0
data.shift_x = 0.0
data.shift_y = 0.0
data.clip_start = 0.10000000149011612
data.clip_end = 1000.0
data.display_size = 1.0
data.dof.use_dof = True
data.dof.focus_object = F
data.dof.aperture_fstop = 1.4
obj = bpy.data.objects.new('vidCamera02', data)
obj.hide_render = False
collection.objects.link(obj)
cameras['vidCamera02'] = obj
obj.parent = camSizecube
obj.matrix_parent_inverse = camSizecube.matrix_world.inverted()

data = bpy.data.cameras.new('vidCamera03')
data.lens = 135.0
data.shift_x = 0.0
data.shift_y = 0.0
data.clip_start = 0.10000000149011612
data.clip_end = 1000.0
data.display_size = 1.0
data.dof.use_dof = True
data.dof.focus_object = F
data.dof.aperture_fstop = 1.4
obj = bpy.data.objects.new('vidCamera03', data)
obj.hide_render = False
collection.objects.link(obj)
cameras['vidCamera03'] = obj
obj.parent = camSizecube
obj.matrix_parent_inverse = camSizecube.matrix_world.inverted()

# new frame
scene.frame_set(30 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035913944244385, -26.03040885925293, 0.33321118354797363
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5845268964767456, -0.0, 0.0015504594193771482
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(31 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035913944244385, -26.02815818786621, 0.33325624465942383
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5845263004302979, -0.0, 0.001550593413412571
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(32 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035913944244385, -26.021228790283203, 0.33339500427246094
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5845246315002441, -0.0, 0.0015510062221437693
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(33 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035913944244385, -26.009334564208984, 0.3336334228515625
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.584521770477295, -0.0, 0.0015517157735303044
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(34 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035913944244385, -25.992172241210938, 0.33397722244262695
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5845175981521606, -1.818989186705422e-12, 0.0015527401119470596
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(35 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035913944244385, -25.969398498535156, 0.33443355560302734
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5845121145248413, -1.818989620386291e-12, 0.001554102054797113
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(36 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035913944244385, -25.94064712524414, 0.3350093364715576
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5845050811767578, -0.0, 0.0015558243030682206
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(37 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035913944244385, -25.905506134033203, 0.33571338653564453
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5844964981079102, -1.818989186705422e-12, 0.0015579347964376211
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(38 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035913944244385, -25.863529205322266, 0.33655428886413574
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5844862461090088, -0.0, 0.001560463453643024
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(39 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035913944244385, -25.814220428466797, 0.3375420570373535
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5844740867614746, 1.8189894035458565e-12, 0.001563444035127759
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(40 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035913944244385, -25.757034301757812, 0.33868908882141113
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5844600200653076, -0.0, 0.0015669155400246382
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(41 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -25.691356658935547, 0.3400089740753174
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5844435691833496, -0.0, 0.001570918713696301
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(42 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -25.61651611328125, 0.34151268005371094
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5844247341156006, -0.0, 0.0015755081549286842
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(43 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -25.531761169433594, 0.3432159423828125
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5844032764434814, -1.818989620386291e-12, 0.001580738346092403
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(44 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -25.436246871948242, 0.3451352119445801
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5843788385391235, 1.8189894035458565e-12, 0.001586673897691071
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(45 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -25.329036712646484, 0.3472895622253418
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5843513011932373, -1.8189894035458565e-12, 0.0015933901304379106
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(46 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -25.209075927734375, 0.3496999740600586
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5843201875686646, -0.0, 0.0016009723767638206
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(47 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -25.0751953125, 0.35239171981811523
obj.scale = 1.000000238418579, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.5842851400375366, -0.0, 0.0016095201717689633
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(48 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -24.92608070373535, 0.35539984703063965
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5842450857162476, 1.818989186705422e-12, 0.0016191485337913036
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(49 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -24.760269165039062, 0.35874509811401367
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.584200143814087, -0.0, 0.0016299914568662643
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(50 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -24.576141357421875, 0.362459659576416
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5841493606567383, -0.0, 0.0016422036569565535
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(51 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -24.37192153930664, 0.3665797710418701
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5840922594070435, -0.0, 0.0016559641808271408
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(52 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -24.145694732666016, 0.37114405632019043
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5840277671813965, -0.0, 0.001671479200012982
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(53 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -23.895435333251953, 0.3762071132659912
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5839544534683228, -0.0, 0.00168898468837142
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(54 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -23.619104385375977, 0.3818094730377197
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0
obj.rotation_euler = 1.5838712453842163, -0.0, 0.001708744908683002
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(55 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035913944244385, -23.314775466918945, 0.38797903060913086
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5837773084640503, -1.818989186705422e-12, 0.0017310517141595483
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(56 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -22.98086166381836, 0.3947486877441406
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5836714506149292, -0.0, 0.0017562014982104301
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(57 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -22.616451263427734, 0.4021487236022949
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5835517644882202, 1.8189894035458565e-12, 0.0017844984540715814
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(58 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -22.221717834472656, 0.4102001190185547
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.5834159851074219, -1.818989186705422e-12, 0.0018161970656365156
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(59 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -21.79840850830078, 0.41883420944213867
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5832650661468506, -0.0, 0.001851466135121882
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(60 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -21.350238800048828, 0.4279756546020508
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5830986499786377, 1.8189894035458565e-12, 0.0018903309246525168
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(61 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -20.883010864257812, 0.43755483627319336
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.582915186882019, 1.8189894035458565e-12, 0.0019326242618262768
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(62 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035913944244385, -20.404273986816406, 0.44739508628845215
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5827172994613647, 1.8189894035458565e-12, 0.0019779715221375227
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(63 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -19.922523498535156, 0.45729732513427734
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.5825085639953613, 1.818989186705422e-12, 0.002025797963142395
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(64 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -19.44610595703125, 0.4671139717102051
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.582290768623352, 3.637977939729975e-12, 0.002075428841635585
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(65 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -18.98223114013672, 0.47674560546875
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5820642709732056, -0.0, 0.002126146573573351
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(66 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -18.53636932373047, 0.4860036373138428
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5818358659744263, -0.0, 0.002177284099161625
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(67 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -18.112110137939453, 0.4948129653930664
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.5816081762313843, -0.0, 0.002228288445621729
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(68 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -17.711366653442383, 0.503187894821167
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.581380009651184, -0.0, 0.0022787023335695267
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(69 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -17.334745407104492, 0.5111169815063477
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5811525583267212, -0.0, 0.0023282135371118784
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(70 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -16.981937408447266, 0.5185446739196777
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5809303522109985, 1.8189894035458565e-12, 0.002376583172008395
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(71 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -16.652055740356445, 0.5254898071289062
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5807141065597534, -0.0, 0.002423664089292288
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(72 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -16.34388542175293, 0.531977653503418
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.5805041790008545, -0.0, 0.0024693626910448074
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(73 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -16.05606460571289, 0.5381374359130859
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5802944898605347, -0.0, 0.0025136247277259827
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(74 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -15.787178039550781, 0.5439131259918213
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.5800905227661133, -0.0, 0.002556436462327838
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(75 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -15.53585147857666, 0.5493118762969971
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5798933506011963, -1.8189894035458565e-12, 0.0025977918412536383
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(76 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -15.300769805908203, 0.5543615818023682
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5797030925750732, -1.818989186705422e-12, 0.002637704601511359
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(77 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -15.080716133117676, 0.5590884685516357
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5795196294784546, 1.818989186705422e-12, 0.002676197327673435
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(78 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -14.87456226348877, 0.5635168552398682
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.5793428421020508, -0.0, 0.002713287714868784
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(79 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -14.681276321411133, 0.567763090133667
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5791661739349365, -1.8189894035458565e-12, 0.002749005099758506
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(80 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -14.499921798706055, 0.5717847347259521
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.578993558883667, 1.8189894035458565e-12, 0.002783391624689102
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(81 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -14.329639434814453, 0.5755610466003418
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5788273811340332, -0.0, 0.0028164631221443415
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(82 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -14.169658660888672, 0.579108476638794
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.5786677598953247, -1.818989186705422e-12, 0.002848266391083598
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(83 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -14.019274711608887, 0.5824432373046875
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5785143375396729, -0.0, 0.0028788188938051462
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(84 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -13.877847671508789, 0.5855793952941895
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.578366994857788, -0.0, 0.0029081522952765226
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(85 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -13.744796752929688, 0.5885300636291504
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5782256126403809, 1.818989186705422e-12, 0.002936307340860367
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(86 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -13.619593620300293, 0.5913064479827881
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5780900716781616, -0.0, 0.0029633003287017345
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(87 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -13.50175952911377, 0.594001054763794
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5779541730880737, -0.0, 0.0029891617596149445
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(88 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -13.390851974487305, 0.5966076850891113
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.577818751335144, -1.8189894035458565e-12, 0.003013914218172431
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(89 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035896062850952, -13.286469459533691, 0.5990610122680664
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0
obj.rotation_euler = 1.577689290046692, -0.0, 0.003037587972357869
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(90 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -13.188241004943848, 0.6013693809509277
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5775656700134277, 1.818989186705422e-12, 0.0030602167826145887
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(91 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -13.0958251953125, 0.603541374206543
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.577447533607483, -0.0, 0.003081812523305416
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(92 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -13.008914947509766, 0.6055841445922852
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0
obj.rotation_euler = 1.577335000038147, -0.0, 0.003102401504293084
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(93 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.927218437194824, 0.60750412940979
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5772277116775513, 1.8189894035458565e-12, 0.0031220074743032455
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(94 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.850475311279297, 0.6093077659606934
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5771257877349854, -1.8189894035458565e-12, 0.00314065208658576
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(95 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.778436660766602, 0.6110007762908936
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5770289897918701, -0.0, 0.0031583576928824186
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(96 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.7108736038208, 0.61258864402771
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.576937198638916, -0.0, 0.0031751450151205063
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(97 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.647577285766602, 0.6140761375427246
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.576850414276123, -0.0, 0.0031910354737192392
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(98 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.588354110717773, 0.6155469417572021
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.5767619609832764, -1.818989186705422e-12, 0.00320604769513011
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(99 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.5330228805542, 0.6170432567596436
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5766689777374268, -0.0, 0.0032202021684497595
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(100 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -12.481403350830078, 0.6184391975402832
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0
obj.rotation_euler = 1.576581358909607, -0.0, 0.003233524737879634
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(101 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -12.433343887329102, 0.6197390556335449
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5764992237091064, -0.0, 0.0032460230868309736
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(102 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.388691902160645, 0.6209464073181152
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5764223337173462, 1.8189894035458565e-12, 0.003257717937231064
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(103 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.347309112548828, 0.622065544128418
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5763505697250366, -0.0, 0.003268635831773281
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(104 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.309063911437988, 0.6230998039245605
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.5762838125228882, 1.818989186705422e-12, 0.003278791904449463
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(105 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.27382755279541, 0.6240527629852295
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5762219429016113, -0.0, 0.0032882047817111015
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(106 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -12.241493225097656, 0.624927282333374
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5761648416519165, -0.0, 0.003296895185485482
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -6.63680362701416, 13.680608749389648
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.47238871455192566, 4.656612873077393e-10, -0.014883739873766899
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(107 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.211950302124023, 0.6257262229919434
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5761123895645142, -0.0, 0.003304865909740329
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0973229855298996, -8.051921844482422, 13.504337310791016
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 0.561062216758728, -0.0, -0.012086339294910431
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(108 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.185094833374023, 0.6264524459838867
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5760644674301147, -1.818989186705422e-12, 0.003312149550765753
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09534787386655807, -8.954425811767578, 13.241421699523926
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 0.6197265982627869, 4.656612873077393e-10, -0.010647728107869625
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(109 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.160825729370117, 0.6271085739135742
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5760210752487183, -1.8189894035458565e-12, 0.003318759612739086
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0930895209312439, -9.655142784118652, 12.909368515014648
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 0.6687546968460083, -0.0, -0.009641148149967194
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(110 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -12.139058113098145, 0.627697229385376
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.575981855392456, -0.0, 0.003324715420603752
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09100016206502914, -10.26089096069336, 12.593334197998047
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 0.71147620677948, -0.0, -0.008868410252034664
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(111 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -12.119699478149414, 0.628220796585083
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.5759470462799072, -1.818989186705422e-12, 0.003330026287585497
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.08884872496128082, -10.773197174072266, 12.238105773925781
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 0.7507408857345581, -0.0, -0.008247015066444874
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(112 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.102672576904297, 0.6286814212799072
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5759161710739136, -0.0, 0.003334705950692296
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.08685116469860077, -11.248863220214844, 11.908283233642578
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 0.7868029475212097, -0.0, -0.0077207316644489765
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(113 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035896062850952, -12.087894439697266, 0.6290810108184814
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758893489837646, -0.0, 0.003338778158649802
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.08488641679286957, -11.649295806884766, 11.539947509765625
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 0.8209539651870728, 4.656612873077393e-10, -0.007286700885742903
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(114 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.075298309326172, 0.6294214725494385
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.575866460800171, -0.0, 0.003342265961691737
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.08301980793476105, -12.02767562866211, 11.188672065734863
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 0.853212833404541, -0.0, -0.006902290042489767
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(115 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.064810752868652, 0.6297051906585693
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758473873138428, -1.8189894035458565e-12, 0.00334517122246325
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.081253781914711, -12.375134468078613, 10.840230941772461
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 0.8838938474655151, -0.0, -0.006565797608345747
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(116 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.056364059448242, 0.6299338340759277
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.5758320093154907, -0.0, 0.0033475146628916264
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07959870249032974, -12.67494010925293, 10.474221229553223
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 0.9134459495544434, -0.0, -0.006279924884438515
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(117 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.049896240234375, 0.6301085948944092
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758202075958252, -0.0, 0.0033493114169687033
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0780041292309761, -12.963787078857422, 10.121591567993164
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 0.9418706297874451, -0.0, -0.006017007865011692
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(118 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.045341491699219, 0.6302316188812256
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758118629455566, 1.818989186705422e-12, 0.0033505780156701803
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07648738473653793, -13.235799789428711, 9.775691986083984
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 0.9692645072937012, -0.0, -0.005778762977570295
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(119 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.04265022277832, 0.6303045749664307
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.575806975364685, 1.818989186705422e-12, 0.0033513265661895275
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07515383511781693, -13.459450721740723, 9.412113189697266
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 0.9958488941192627, -0.0, -0.005583664868026972
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(120 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07385900616645813, -13.676605224609375, 9.059093475341797
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.021693468093872, -2.3283064365386963e-10, -0.005400338210165501
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(121 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0725996345281601, -13.887815475463867, 8.715739250183105
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.0468276739120483, 2.3283064365386963e-10, -0.005227531306445599
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(122 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07150555402040482, -14.067523002624512, 8.367660522460938
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.071245789527893, 2.3283064365386963e-10, -0.0050829811953008175
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(123 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07054547965526581, -14.221805572509766, 8.017230987548828
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.0950950384140015, -0.0, -0.0049603343941271305
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(124 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06960831582546234, -14.372405052185059, 7.675169467926025
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.118442177772522, -0.0, -0.004843154922127724
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(125 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06869281828403473, -14.519524574279785, 7.3410115242004395
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.1412897109985352, -2.3283061589829401e-10, -0.00473103066906333
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(126 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06793750822544098, -14.6414794921875, 7.006525993347168
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.163547396659851, 1.1641532182693481e-10, -0.0046400390565395355
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(127 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06735778599977493, -14.735868453979492, 6.670472145080566
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.185302972793579, 1.1641532182693481e-10, -0.004570978228002787
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(128 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06679059565067291, -14.828214645385742, 6.3416852951049805
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2066915035247803, -1.1641532182693481e-10, -0.004504261538386345
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(129 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06623553484678268, -14.918588638305664, 6.019926071166992
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2277034521102905, -0.0, -0.0044397711753845215
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(130 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06569227576255798, -15.007039070129395, 5.705010890960693
obj.scale = 1.000000238418579, 1.0, 1.0
obj.rotation_euler = 1.2483280897140503, -0.0, -0.004377403762191534
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(131 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06543957442045212, -15.055838584899902, 5.389097213745117
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.2683074474334717, -1.1641533570472262e-10, -0.004346431698650122
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(132 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06525009870529175, -15.095767974853516, 5.078334808349609
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2879356145858765, -0.0, -0.004322384018450975
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(133 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06506471335887909, -15.134834289550781, 4.7742815017700195
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3072574138641357, -0.0, -0.0042989784851670265
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(134 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06488338857889175, -15.173044204711914, 4.476898670196533
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.3262546062469482, -0.0, -0.004276202525943518
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(135 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06470614671707153, -15.210396766662598, 4.186192035675049
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.344907522201538, -0.0, -0.004254048690199852
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(136 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06470271944999695, -15.226120948791504, 3.9011118412017822
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3629896640777588, -0.0, -0.004249430727213621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(137 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06487684696912766, -15.219755172729492, 3.6217246055603027
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3805434703826904, 5.820766091346741e-11, -0.004262648522853851
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(138 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06504663079977036, -15.21354866027832, 3.3493258953094482
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3977876901626587, -0.0, -0.004275547806173563
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(139 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06521192938089371, -15.207505226135254, 3.084103584289551
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.414691686630249, -0.0, -0.004288116004317999
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(140 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06537260860204697, -15.201631546020508, 2.8263049125671387
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4312223196029663, -0.0, -0.004300342407077551
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(141 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06552846729755402, -15.19593334197998, 2.5762381553649902
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4473432302474976, -0.0, -0.004312211647629738
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(142 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06569646298885345, -15.188468933105469, 2.3344976902008057
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.462986707687378, 2.9103833926180656e-11, -0.0043253907933831215
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(143 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06615467369556427, -15.147665977478027, 2.104733467102051
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4777134656906128, -0.0, -0.004367290996015072
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(144 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0665946900844574, -15.10848331451416, 1.8840916156768799
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4919689893722534, 2.9103833926180656e-11, -0.004407740663737059
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(145 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06701494753360748, -15.071060180664062, 1.673356056213379
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5056840181350708, 2.9103830456733704e-11, -0.0044465698301792145
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(146 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06741344183683395, -15.035574913024902, 1.4735348224639893
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5187747478485107, -1.4551915228366852e-11, -0.004483566619455814
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(147 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06778757274150848, -15.00225830078125, 1.2859301567077637
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5311379432678223, -0.0, -0.004518461413681507
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(148 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0681338831782341, -14.971420288085938, 1.1122770309448242
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5426416397094727, -0.0, -0.004550898913294077
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(149 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06844767183065414, -14.94347858428955, 0.9549336433410645
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.553112506866455, -0.0, -0.004580406472086906
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(150 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0687222108244896, -14.919031143188477, 0.8172674179077148
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5623093843460083, -0.0, -0.0046063135378062725
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(151 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06894747167825699, -14.898972511291504, 0.7043132781982422
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5698790550231934, -0.0, -0.004627633839845657
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(152 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06910714507102966, -14.884753227233887, 0.6242465972900391
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5752571821212769, -0.0, -0.004642781335860491
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(153 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019723236560821533, -16.643054962158203, 7.788717746734619
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1676658391952515, -2.9103830456733704e-11, 0.0011850716546177864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(154 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.016693830490112305, -17.09462547302246, 7.782711982727051
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1775362491607666, -0.0, 0.0009765531285665929
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(155 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.014614999294281006, -17.487403869628906, 7.729654312133789
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1881206035614014, -2.9103833926180656e-11, 0.0008357434417121112
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(156 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.013341844081878662, -17.83344268798828, 7.634894371032715
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1994658708572388, -0.0, 0.0007481352076865733
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(157 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.012184977531433105, -18.147869110107422, 7.54879093170166
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.2094825506210327, -0.0, 0.0006714264745824039
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(158 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01157301664352417, -18.426103591918945, 7.43959379196167
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.2197004556655884, -0.0, 0.000628076319117099
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(159 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.011064410209655762, -18.68219757080078, 7.334704399108887
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.2291096448898315, -0.0, 0.0005922426353208721
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(160 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.010590553283691406, -18.920801162719727, 7.236978530883789
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.2377018928527832, -0.0, 0.0005597298732027411
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(161 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01014631986618042, -19.144481658935547, 7.145364761352539
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2456073760986328, 1.4551915228366852e-11, 0.0005299858166836202
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(162 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009877443313598633, -19.351444244384766, 7.050433158874512
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2532697916030884, -0.0, 0.0005104232695885003
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(163 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009717404842376709, -19.545021057128906, 6.95511531829834
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2606264352798462, 1.4551915228366852e-11, 0.0004971798043698072
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(164 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009565114974975586, -19.729148864746094, 6.864450931549072
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.267521619796753, -0.0, 0.0004848206590395421
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(165 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009419739246368408, -19.904972076416016, 6.777874946594238
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2740137577056885, -0.0, 0.0004732346860691905
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(166 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.00928044319152832, -20.073463439941406, 6.694910049438477
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2801522016525269, -1.4551915228366852e-11, 0.0004623232234735042
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(167 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009146451950073242, -20.23544692993164, 6.615148544311523
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.2859779596328735, -0.0, 0.0004520006768871099
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(168 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.00901937484741211, -20.39158821105957, 6.538144111633301
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.291529893875122, -7.275958481545164e-12, 0.0004423078498803079
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(169 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009033381938934326, -20.539222717285156, 6.457280158996582
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2970811128616333, -0.0, 0.0004398105083964765
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(170 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009046971797943115, -20.682323455810547, 6.378898620605469
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3024026155471802, -0.0, 0.00043742460547946393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(171 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009060204029083252, -20.821352005004883, 6.302748680114746
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3075170516967773, -0.0, 0.00043513934360817075
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(172 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009073078632354736, -20.956714630126953, 6.228607177734375
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3124449253082275, -1.4551915228366852e-11, 0.00043294302304275334
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(173 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.00908571481704712, -21.088768005371094, 6.156276702880859
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3172035217285156, -0.0, 0.00043083124910481274
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(174 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009098052978515625, -21.21783447265625, 6.085583209991455
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3218083381652832, -0.0, 0.0004287920019123703
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(175 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009110033512115479, -21.344200134277344, 6.016369819641113
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3262730836868286, 7.275958481545164e-12, 0.00042681474587880075
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(176 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009121835231781006, -21.468116760253906, 5.9484968185424805
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3306097984313965, -0.0, 0.00042490081978030503
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(177 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009133458137512207, -21.589813232421875, 5.881838798522949
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.334829330444336, 7.275957614183426e-12, 0.00042304411181248724
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(178 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.00922393798828125, -21.707904815673828, 5.813467502593994
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3390475511550903, -0.0, 0.00042491077329032123
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(179 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009332001209259033, -21.823810577392578, 5.745461940765381
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3431905508041382, 7.275958481545164e-12, 0.0004276057588867843
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(180 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009438633918762207, -21.93808937072754, 5.678411483764648
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3472402095794678, -0.0, 0.00043023889884352684
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(181 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009543895721435547, -22.050891876220703, 5.612227439880371
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3512035608291626, -0.0, 0.00043281150283291936
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(182 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009647786617279053, -22.162351608276367, 5.546829700469971
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3550869226455688, -0.0, 0.0004353225522208959
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(183 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009750664234161377, -22.272602081298828, 5.482142925262451
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.358896255493164, -0.0, 0.00043778674444183707
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(184 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009852468967437744, -22.381752014160156, 5.418101787567139
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.362636685371399, 7.275957614183426e-12, 0.00044020029599778354
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(185 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.00995337963104248, -22.489910125732422, 5.354642391204834
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.366313099861145, -0.0, 0.0004425701918080449
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(186 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.010053515434265137, -22.597171783447266, 5.291708946228027
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3699297904968262, -7.275957614183426e-12, 0.0004449007974471897
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(187 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.010152757167816162, -22.703624725341797, 5.229249954223633
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.373490571975708, -7.275957614183426e-12, 0.00044718594290316105
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(188 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.010251402854919434, -22.809350967407227, 5.1672163009643555
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3769992589950562, -0.0, 0.00044943796820007265
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(189 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.010404825210571289, -22.91361427307129, 5.104209899902344
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3805092573165894, -0.0, 0.00045408858568407595
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(190 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.010590314865112305, -23.01681900024414, 5.040746688842773
obj.scale = 1.0000001192092896, 1.0000001192092896, 0.9999999403953552
obj.rotation_euler = 1.3840030431747437, -0.0, 0.0004601113614626229
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(191 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.010774850845336914, -23.1195125579834, 4.977596282958984
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3874530792236328, -0.0, 0.0004660494450945407
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(192 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.010958492755889893, -23.221755981445312, 4.9147233963012695
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.390861988067627, -7.275958481545164e-12, 0.0004719056305475533
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(193 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.011141538619995117, -23.3236026763916, 4.852094650268555
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.394232153892517, -0.0, 0.0004776930727530271
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(194 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.011323988437652588, -23.425106048583984, 4.789676666259766
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3975657224655151, -0.0, 0.00048341182991862297
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(195 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01150578260421753, -23.526309967041016, 4.727443218231201
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.400864601135254, -7.275957614183426e-12, 0.000489059544634074
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(196 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.011687219142913818, -23.627262115478516, 4.665365219116211
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4041309356689453, -0.0, 0.0004946490516886115
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(197 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01186823844909668, -23.727998733520508, 4.603418350219727
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4073660373687744, -0.0, 0.000500178022775799
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(198 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.012048900127410889, -23.828561782836914, 4.541578769683838
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4105716943740845, -0.0, 0.0005056489026173949
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(199 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.012229502201080322, -23.928983688354492, 4.479825973510742
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.41374933719635, -0.0, 0.0005110741476528347
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(200 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.012409746646881104, -24.029300689697266, 4.418138027191162
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4169001579284668, -0.0, 0.0005164416506886482
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(201 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.012821972370147705, -24.18108367919922, 4.322027206420898
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4217357635498047, 7.275958481545164e-12, 0.0005302474019117653
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(202 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.013224303722381592, -24.324138641357422, 4.2311692237854
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.426255464553833, -0.0, 0.000543669331818819
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(203 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.013607025146484375, -24.460247039794922, 4.144722938537598
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4305120706558228, 7.275958481545164e-12, 0.0005562907317653298
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(204 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.013973474502563477, -24.590538024902344, 4.061971664428711
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4345473051071167, 7.275958481545164e-12, 0.000568245304748416
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(205 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01432579755783081, -24.715818405151367, 3.98240327835083
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4383913278579712, -7.275957614183426e-12, 0.0005796199548058212
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(206 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.014665722846984863, -24.836685180664062, 3.90563702583313
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4420669078826904, -7.275957614183426e-12, 0.0005904856370761991
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(207 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.014994561672210693, -24.953601837158203, 3.8313803672790527
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4455918073654175, -0.0, 0.0006008970667608082
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(208 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.015313267707824707, -25.066925048828125, 3.7594048976898193
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4489798545837402, -0.0, 0.0006108946399763227
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(209 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.015663325786590576, -25.17676544189453, 3.689249277114868
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.452252745628357, -7.275957614183426e-12, 0.0006221334915608168
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(210 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.016108393669128418, -25.2830753326416, 3.6203322410583496
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4554353952407837, 7.275957614183426e-12, 0.0006371209165081382
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(211 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.016541481018066406, -25.386518478393555, 3.5532727241516113
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4585089683532715, -7.275957614183426e-12, 0.0006515845307148993
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(212 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01696312427520752, -25.48725128173828, 3.4879698753356934
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4614800214767456, -7.275957614183426e-12, 0.0006655525648966432
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(213 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.017374098300933838, -25.585403442382812, 3.4243407249450684
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4643542766571045, -0.0, 0.0006790621555410326
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(214 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.017774581909179688, -25.681079864501953, 3.362316370010376
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4671366214752197, -0.0, 0.0006921268068253994
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(215 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.018165171146392822, -25.774372100830078, 3.3018364906311035
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4698312282562256, -7.275956746821688e-12, 0.0007047757389955223
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(216 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01854604482650757, -25.865354537963867, 3.2428555488586426
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4724417924880981, -7.275957614183426e-12, 0.0007170218741521239
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(217 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.018917500972747803, -25.954090118408203, 3.185330867767334
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4749716520309448, -0.0, 0.0007288824999704957
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(218 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019279778003692627, -26.040626525878906, 3.1292314529418945
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4774233102798462, -0.0, 0.0007403723429888487
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(219 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01967442035675049, -26.12496566772461, 3.074467182159424
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4798015356063843, -0.0, 0.000753088213969022
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(220 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.020199716091156006, -26.20703887939453, 3.0208675861358643
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0
obj.rotation_euler = 1.4821137189865112, -0.0, 0.0007707737386226654
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(221 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.02071171998977661, -26.287017822265625, 2.9686362743377686
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4843538999557495, -7.275956746821688e-12, 0.0007879059994593263
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(222 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.021210312843322754, -26.364919662475586, 2.91776180267334
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4865237474441528, -1.4551915228366852e-11, 0.0008044891874305904
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(223 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.02169579267501831, -26.440753936767578, 2.868236541748047
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4886244535446167, -7.275957614183426e-12, 0.0008205429185181856
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(224 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.022167980670928955, -26.514530181884766, 2.820056915283203
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4906572103500366, -0.0, 0.0008360684150829911
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(225 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.02262699604034424, -26.58624267578125, 2.773224353790283
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4926230907440186, -0.0, 0.0008510783081874251
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(226 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.02307283878326416, -26.655887603759766, 2.727741241455078
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4945226907730103, -7.275957614183426e-12, 0.0008655805722810328
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(227 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.023505330085754395, -26.72345542907715, 2.683614730834961
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.496356725692749, -0.0, 0.000879575964063406
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(228 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.023924410343170166, -26.788930892944336, 2.640855073928833
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4981255531311035, -0.0, 0.0008930699550546706
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(229 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.024329960346221924, -26.852291107177734, 2.5994768142700195
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4998294115066528, -0.0, 0.0009060656884685159
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(230 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.024927139282226562, -26.913740158081055, 2.559852361679077
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5014559030532837, 7.275957614183426e-12, 0.0009261855739168823
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(231 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.02558457851409912, -26.973100662231445, 2.521775245666504
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5030131340026855, -7.275957614183426e-12, 0.0009485211339779198
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(232 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.026217341423034668, -27.030242919921875, 2.4851207733154297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.50450599193573, -0.0, 0.0009699254296720028
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(233 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.026825129985809326, -27.085124969482422, 2.4499166011810303
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5059341192245483, -0.0, 0.000990399974398315
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(234 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.027407288551330566, -27.1376953125, 2.4161934852600098
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5072969198226929, 7.275957614183426e-12, 0.0010099334176629782
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(235 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.02796339988708496, -27.187908172607422, 2.3839855194091797
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5085939168930054, 7.275958481545164e-12, 0.0010285224998369813
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(236 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.028492629528045654, -27.235694885253906, 2.3533310890197754
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5098240375518799, 7.275957614183426e-12, 0.001046149292960763
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(237 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.028994321823120117, -27.28099822998047, 2.3242721557617188
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.510986328125, -0.0, 0.0010628019226714969
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(238 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.02946758270263672, -27.32373809814453, 2.296855926513672
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5120794773101807, -0.0, 0.0010784598998725414
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(239 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.02991163730621338, -27.363832473754883, 2.2711360454559326
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5131021738052368, 7.275957614183426e-12, 0.00109310750849545
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(240 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.030612647533416748, -27.401782989501953, 2.2481658458709717
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5140173435211182, -0.0, 0.0011171761434525251
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(241 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.03168749809265137, -27.437725067138672, 2.228419542312622
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.514809012413025, -7.275957614183426e-12, 0.0011548869078978896
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(242 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.03267073631286621, -27.470603942871094, 2.210357427597046
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.515531301498413, -7.275957614183426e-12, 0.0011892970651388168
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(243 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.03355860710144043, -27.500293731689453, 2.194046974182129
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5161821842193604, 7.275957614183426e-12, 0.0012202986981719732
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(244 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.034346818923950195, -27.52664566040039, 2.17956805229187
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.5167587995529175, -0.0, 0.0012477650307118893
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(245 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.03503072261810303, -27.549514770507812, 2.1670045852661133
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5172582864761353, 7.275957614183426e-12, 0.0012715536868199706
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(246 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.03560507297515869, -27.568723678588867, 2.15645170211792
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5176771879196167, -0.0, 0.0012915011029690504
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(247 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.036064326763153076, -27.58407974243164, 2.1480166912078857
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5180116891860962, -0.0, 0.0013074312591925263
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(248 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.03640180826187134, -27.59536361694336, 2.141817331314087
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5182572603225708, 7.275958481545164e-12, 0.0013191263424232602
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(249 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.036610305309295654, -27.602336883544922, 2.137986183166504
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5184088945388794, 7.275957614183426e-12, 0.0013263466535136104
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(250 + frame)
obj = cameras['vidCamera01']
obj.location = 0.0403590202331543, -12.041766166687012, 0.6303284168243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5758053064346313, -0.0, 0.0033515726681798697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -14.879022598266602, 0.591977596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5774275064468384, -3.637978807091713e-12, -0.004648895002901554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.03668183088302612, -27.60472869873047, 2.1366724967956543
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.5184608697891235, -0.0, 0.0013288228074088693
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# markers
scene.timeline_markers.clear()
marker = scene.timeline_markers.new('')
marker.frame = 1 + frame
marker.camera = bpy.data.objects.get('picCamera01')

marker = scene.timeline_markers.new('')
marker.frame = 30 + frame
marker.camera = cameras.get('vidCamera01')

marker = scene.timeline_markers.new('')
marker.frame = 106 + frame
marker.camera = cameras.get('vidCamera02')

marker = scene.timeline_markers.new('')
marker.frame = 153 + frame
marker.camera = cameras.get('vidCamera03')

# transform
camSizecube.scale = LocatedCube.scale
camSizecube.location = LocatedCube.location
curScene = bpy.context.window.scene
curScene.frame_start = 30
curScene.frame_end = 250

