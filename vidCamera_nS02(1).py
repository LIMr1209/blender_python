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
data.lens = 120.0
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
data.lens = 98.0
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
obj.location = -8.916234016418457, -10.928481101989746, 0.6861481666564941
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6145563125610352, -0.0, -0.6843439340591431
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(31 + frame)
obj = cameras['vidCamera01']
obj.location = -8.914518356323242, -10.92800521850586, 0.6860671043395996
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.6145665645599365, -0.0, -0.6842709183692932
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(32 + frame)
obj = cameras['vidCamera01']
obj.location = -8.909235000610352, -10.926541328430176, 0.6858181953430176
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.614598035812378, -0.0, -0.6840462684631348
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(33 + frame)
obj = cameras['vidCamera01']
obj.location = -8.900169372558594, -10.924028396606445, 0.6853909492492676
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.614652156829834, -0.0, -0.6836602687835693
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(34 + frame)
obj = cameras['vidCamera01']
obj.location = -8.8870849609375, -10.920402526855469, 0.6847743988037109
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.6147303581237793, -1.862645149230957e-09, -0.6831024289131165
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(35 + frame)
obj = cameras['vidCamera01']
obj.location = -8.86972427368164, -10.9155912399292, 0.6839561462402344
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.614834189414978, -1.862645149230957e-09, -0.6823610067367554
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(36 + frame)
obj = cameras['vidCamera01']
obj.location = -8.84780502319336, -10.909517288208008, 0.6829228401184082
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.6149656772613525, -0.0, -0.6814226508140564
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(37 + frame)
obj = cameras['vidCamera01']
obj.location = -8.821017265319824, -10.902092933654785, 0.6816604137420654
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.615126609802246, -1.8626449271863521e-09, -0.6802725791931152
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(38 + frame)
obj = cameras['vidCamera01']
obj.location = -8.789016723632812, -10.893223762512207, 0.680152177810669
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.6153196096420288, -0.0, -0.6788938045501709
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(39 + frame)
obj = cameras['vidCamera01']
obj.location = -8.75142765045166, -10.882806777954102, 0.6783804893493652
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.6155471801757812, -1.862645371275562e-09, -0.6772672533988953
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(40 + frame)
obj = cameras['vidCamera01']
obj.location = -8.707805633544922, -10.87072467803955, 0.6770493984222412
obj.scale = 1.000000238418579, 1.000000238418579, 1.0
obj.rotation_euler = 1.615760326385498, -0.0, -0.6753702759742737
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(41 + frame)
obj = cameras['vidCamera01']
obj.location = -8.657697677612305, -10.856850624084473, 0.6758158206939697
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6159852743148804, -1.862645149230957e-09, -0.6731786727905273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(42 + frame)
obj = cameras['vidCamera01']
obj.location = -8.60059928894043, -10.841039657592773, 0.674410343170166
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.6162428855895996, -0.0, -0.6706649661064148
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(43 + frame)
obj = cameras['vidCamera01']
obj.location = -8.535933494567871, -10.82313346862793, 0.6728181838989258
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.6165363788604736, -1.862645149230957e-09, -0.6677970886230469
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(44 + frame)
obj = cameras['vidCamera01']
obj.location = -8.463061332702637, -10.80295467376709, 0.6710240840911865
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.616869568824768, 1.862645371275562e-09, -0.6645382046699524
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(45 + frame)
obj = cameras['vidCamera01']
obj.location = -8.381264686584473, -10.780305862426758, 0.6690104007720947
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.6172465085983276, -0.0, -0.6608455777168274
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(46 + frame)
obj = cameras['vidCamera01']
obj.location = -8.289741516113281, -10.754962921142578, 0.666757345199585
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6176718473434448, -1.862645149230957e-09, -0.6566699743270874
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(47 + frame)
obj = cameras['vidCamera01']
obj.location = -8.18757438659668, -10.726693153381348, 0.666175127029419
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.6180083751678467, -1.862645149230957e-09, -0.6519523859024048
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(48 + frame)
obj = cameras['vidCamera01']
obj.location = -8.07376766204834, -10.695215225219727, 0.6667473316192627
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6182960271835327, 3.7252898543727042e-09, -0.6466267108917236
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(49 + frame)
obj = cameras['vidCamera01']
obj.location = -7.947216510772705, -10.660213470458984, 0.6673836708068848
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.6186189651489258, -1.862645149230957e-09, -0.6406164765357971
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(50 + frame)
obj = cameras['vidCamera01']
obj.location = -7.806686878204346, -10.621343612670898, 0.6680903434753418
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6189815998077393, -1.862645149230957e-09, -0.6338317394256592
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(51 + frame)
obj = cameras['vidCamera01']
obj.location = -7.65082311630249, -10.57823371887207, 0.6688740253448486
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.619388461112976, -0.0, -0.626167356967926
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(52 + frame)
obj = cameras['vidCamera01']
obj.location = -7.478188991546631, -10.530500411987305, 0.6711695194244385
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6197346448898315, -0.0, -0.617502748966217
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(53 + frame)
obj = cameras['vidCamera01']
obj.location = -7.287322521209717, -10.477784156799316, 0.6791925430297852
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6196928024291992, -0.0, -0.6077009439468384
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(54 + frame)
obj = cameras['vidCamera01']
obj.location = -7.0765700340271, -10.419574737548828, 0.6880509853363037
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.6196397542953491, -0.0, -0.5966028571128845
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(55 + frame)
obj = cameras['vidCamera01']
obj.location = -6.8444647789001465, -10.355467796325684, 0.6978073120117188
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6195725202560425, -0.0, -0.5840356349945068
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(56 + frame)
obj = cameras['vidCamera01']
obj.location = -6.589807987213135, -10.285135269165039, 0.7087159156799316
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6194703578948975, 1.862645149230957e-09, -0.5698180198669434
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(57 + frame)
obj = cameras['vidCamera01']
obj.location = -6.312634468078613, -10.208718299865723, 0.733400821685791
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6182782649993896, -0.0, -0.5538081526756287
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(58 + frame)
obj = cameras['vidCamera01']
obj.location = -6.012397289276123, -10.12594223022461, 0.7601394653320312
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6169242858886719, -0.0, -0.535819947719574
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(59 + frame)
obj = cameras['vidCamera01']
obj.location = -5.690426826477051, -10.037175178527832, 0.7888139486312866
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6153959035873413, -0.0, -0.5157521963119507
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(60 + frame)
obj = cameras['vidCamera01']
obj.location = -5.350846290588379, -9.943680763244629, 0.8311455249786377
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6126247644424438, -0.0, -0.49367284774780273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(61 + frame)
obj = cameras['vidCamera01']
obj.location = -4.997805118560791, -9.846577644348145, 0.8843286037445068
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.6087607145309448, 9.313225746154785e-10, -0.469683438539505
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(62 + frame)
obj = cameras['vidCamera01']
obj.location = -4.636072158813477, -9.747082710266113, 0.93882155418396
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.604593276977539, -0.0, -0.4439678490161896
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(63 + frame)
obj = cameras['vidCamera01']
obj.location = -4.274415969848633, -9.647754669189453, 1.007047176361084
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989060401916504, -0.0, -0.41705742478370667
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(64 + frame)
obj = cameras['vidCamera01']
obj.location = -3.919548511505127, -9.550463676452637, 1.0903337001800537
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.591465950012207, -4.656613428188905e-10, -0.389443039894104
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(65 + frame)
obj = cameras['vidCamera01']
obj.location = -3.5740232467651367, -9.455734252929688, 1.171427607536316
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5838851928710938, 4.656612873077393e-10, -0.3613756000995636
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(66 + frame)
obj = cameras['vidCamera01']
obj.location = -3.244523048400879, -9.365506172180176, 1.2589919567108154
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5753116607666016, -1.1641532182693481e-10, -0.33349382877349854
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(67 + frame)
obj = cameras['vidCamera01']
obj.location = -2.9379982948303223, -9.281862258911133, 1.3681765794754028
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.564178466796875, 1.1641532182693481e-10, -0.3065531253814697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(68 + frame)
obj = cameras['vidCamera01']
obj.location = -2.6484646797180176, -9.202856063842773, 1.471308946609497
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.5533006191253662, -0.0, -0.2802151143550873
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(69 + frame)
obj = cameras['vidCamera01']
obj.location = -2.3763561248779297, -9.128602981567383, 1.5682345628738403
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5427645444869995, -0.0, -0.25466758012771606
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(70 + frame)
obj = cameras['vidCamera01']
obj.location = -2.1318020820617676, -9.062172889709473, 1.6839947700500488
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5299739837646484, -0.0, -0.2310411036014557
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(71 + frame)
obj = cameras['vidCamera01']
obj.location = -1.9088525772094727, -9.001785278320312, 1.806015968322754
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5162674188613892, -9.313225746154785e-10, -0.20895734429359436
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(72 + frame)
obj = cameras['vidCamera01']
obj.location = -1.7005770206451416, -8.945371627807617, 1.9200061559677124
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.5032199621200562, -9.31322685637781e-10, -0.18786512315273285
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(73 + frame)
obj = cameras['vidCamera01']
obj.location = -1.5060516595840454, -8.892683029174805, 2.02647066116333
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4908363819122314, -0.0, -0.16776661574840546
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(74 + frame)
obj = cameras['vidCamera01']
obj.location = -1.3292768001556396, -8.844911575317383, 2.133495330810547
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4782919883728027, -0.0, -0.14917080104351044
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(75 + frame)
obj = cameras['vidCamera01']
obj.location = -1.1836023330688477, -8.805984497070312, 2.263399362564087
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4632072448730469, -0.0, -0.1336081176996231
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(76 + frame)
obj = cameras['vidCamera01']
obj.location = -1.0473436117172241, -8.769573211669922, 2.3849070072174072
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4489868879318237, -9.313225746154785e-10, -0.11886624991893768
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(77 + frame)
obj = cameras['vidCamera01']
obj.location = -0.9197955131530762, -8.735489845275879, 2.4986469745635986
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.4355913400650024, 9.31322685637781e-10, -0.10490754246711731
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(78 + frame)
obj = cameras['vidCamera01']
obj.location = -0.8003034591674805, -8.703559875488281, 2.6052029132843018
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4229789972305298, 9.313225746154785e-10, -0.0916934385895729
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(79 + frame)
obj = cameras['vidCamera01']
obj.location = -0.6882691383361816, -8.673622131347656, 2.705108642578125
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4111078977584839, -0.0, -0.07918605953454971
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(80 + frame)
obj = cameras['vidCamera01']
obj.location = -0.5956305861473083, -8.649101257324219, 2.8098485469818115
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3987904787063599, -0.0, -0.06875761598348618
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(81 + frame)
obj = cameras['vidCamera01']
obj.location = -0.527769923210144, -8.631545066833496, 2.925048828125
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3854633569717407, -0.0, -0.06106829270720482
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(82 + frame)
obj = cameras['vidCamera01']
obj.location = -0.4640154242515564, -8.61505126953125, 3.033278465270996
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3729522228240967, -0.0, -0.053809020668268204
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(83 + frame)
obj = cameras['vidCamera01']
obj.location = -0.4040839672088623, -8.599546432495117, 3.1350181102752686
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3612051010131836, -9.313225746154785e-10, -0.0469544492661953
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(84 + frame)
obj = cameras['vidCamera01']
obj.location = -0.347723126411438, -8.584966659545898, 3.230696201324463
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3501745462417603, -9.313225746154785e-10, -0.04048159345984459
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(85 + frame)
obj = cameras['vidCamera01']
obj.location = -0.29469963908195496, -8.571249008178711, 3.320708990097046
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.339815378189087, 4.656612873077393e-10, -0.034368809312582016
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(86 + frame)
obj = cameras['vidCamera01']
obj.location = -0.2448042631149292, -8.558340072631836, 3.4054112434387207
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3300868272781372, -0.0, -0.02859637886285782
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(87 + frame)
obj = cameras['vidCamera01']
obj.location = -0.19784456491470337, -8.546192169189453, 3.4851303100585938
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3209502696990967, 4.656612873077393e-10, -0.023145893588662148
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(88 + frame)
obj = cameras['vidCamera01']
obj.location = -0.15364396572113037, -8.534757614135742, 3.5601651668548584
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3123700618743896, -0.0, -0.018000204116106033
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(89 + frame)
obj = cameras['vidCamera01']
obj.location = -0.127794086933136, -8.528417587280273, 3.636955976486206
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3037787675857544, -0.0, -0.014983383007347584
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(90 + frame)
obj = cameras['vidCamera01']
obj.location = -0.11452442407608032, -8.525555610656738, 3.7135536670684814
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.29534912109375, -0.0, -0.013432267121970654
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(91 + frame)
obj = cameras['vidCamera01']
obj.location = -0.10204005241394043, -8.522863388061523, 3.785618543624878
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2874499559402466, 4.656612873077393e-10, -0.01197193842381239
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(92 + frame)
obj = cameras['vidCamera01']
obj.location = -0.09029942750930786, -8.520332336425781, 3.8533902168273926
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2800501585006714, -0.0, -0.010597716085612774
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(93 + frame)
obj = cameras['vidCamera01']
obj.location = -0.07926303148269653, -8.517951965332031, 3.9170966148376465
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2731202840805054, -0.0, -0.009305141866207123
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(94 + frame)
obj = cameras['vidCamera01']
obj.location = -0.06889587640762329, -8.515716552734375, 3.9769399166107178
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2666341066360474, -0.0, -0.008090263232588768
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(95 + frame)
obj = cameras['vidCamera01']
obj.location = -0.05916410684585571, -8.513617515563965, 4.033115386962891
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2605664730072021, -0.0, -0.006949239876121283
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(96 + frame)
obj = cameras['vidCamera01']
obj.location = -0.050037264823913574, -8.511649131774902, 4.085799217224121
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.2548949718475342, 1.1641533570472262e-10, -0.005878614727407694
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(97 + frame)
obj = cameras['vidCamera01']
obj.location = -0.04148656129837036, -8.509805679321289, 4.135157108306885
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.2495983839035034, -0.0, -0.004875111393630505
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(98 + frame)
obj = cameras['vidCamera01']
obj.location = -0.03348571062088013, -8.508079528808594, 4.181341171264648
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.2446573972702026, -0.0, -0.003935735672712326
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(99 + frame)
obj = cameras['vidCamera01']
obj.location = -0.026010334491729736, -8.506467819213867, 4.224492073059082
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.2400542497634888, -5.820766091346741e-11, -0.003057704772800207
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(100 + frame)
obj = cameras['vidCamera01']
obj.location = -0.019036471843719482, -8.504963874816895, 4.2647480964660645
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.2357715368270874, -5.820766091346741e-11, -0.0022382757160812616
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(101 + frame)
obj = cameras['vidCamera01']
obj.location = -0.012543678283691406, -8.50356388092041, 4.302227020263672
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2317944765090942, -2.9103830456733704e-11, -0.0014751090202480555
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(102 + frame)
obj = cameras['vidCamera01']
obj.location = -0.006511032581329346, -8.502263069152832, 4.33704948425293
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2281084060668945, 1.4551915228366852e-11, -0.0007658015820197761
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(103 + frame)
obj = cameras['vidCamera01']
obj.location = -0.0009201765060424805, -8.501056671142578, 4.369322776794434
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2246997356414795, 3.637979240772582e-12, -0.00010824437049450353
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(104 + frame)
obj = cameras['vidCamera01']
obj.location = 0.004246830940246582, -8.499942779541016, 4.399148464202881
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.2215564250946045, 1.4551916963090328e-11, 0.0004996287170797586
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(105 + frame)
obj = cameras['vidCamera01']
obj.location = 0.00900721549987793, -8.498916625976562, 4.4266276359558105
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2186660766601562, -0.0, 0.0010598053922876716
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(106 + frame)
obj = cameras['vidCamera01']
obj.location = 0.013375818729400635, -8.497974395751953, 4.451844692230225
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 1.2160186767578125, -0.0, 0.0015739977825433016
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09878773242235184, -3.514857292175293, 4.229236125946045
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 0.8768500089645386, 9.313225746154785e-10, -0.028098363429307938
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(107 + frame)
obj = cameras['vidCamera01']
obj.location = 0.017367005348205566, -8.497114181518555, 4.474883079528809
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.2136039733886719, -0.0, 0.00204386655241251
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09834393858909607, -3.9779129028320312, 4.197906494140625
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 0.9419590830802917, -9.313225746154785e-10, -0.024717463180422783
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(108 + frame)
obj = cameras['vidCamera01']
obj.location = 0.02099519968032837, -8.496331214904785, 4.495826721191406
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.2114121913909912, -0.0, 0.0024710833095014095
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09792439639568329, -4.280811309814453, 4.166858196258545
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 0.9814221262931824, -9.313225746154785e-10, -0.02287120930850506
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(109 + frame)
obj = cameras['vidCamera01']
obj.location = 0.024273991584777832, -8.495624542236328, 4.5147528648376465
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2094343900680542, 1.1641532182693481e-10, 0.0028572245500981808
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0972018837928772, -4.526338577270508, 4.110457420349121
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.0158430337905884, -0.0, -0.021471429616212845
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(110 + frame)
obj = cameras['vidCamera01']
obj.location = 0.027214884757995605, -8.494989395141602, 4.531728744506836
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0
obj.rotation_euler = 1.207662582397461, 1.1641530794914701e-10, 0.003203626722097397
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09656469523906708, -4.742865562438965, 4.060717582702637
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.0443391799926758, 9.313225746154785e-10, -0.020357178524136543
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(111 + frame)
obj = cameras['vidCamera01']
obj.location = 0.029830217361450195, -8.494426727294922, 4.546825885772705
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.2060890197753906, -0.0, 0.0035117235966026783
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09580939263105392, -4.935338020324707, 4.000316143035889
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.070815920829773, -9.313225746154785e-10, -0.019410498440265656
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(112 + frame)
obj = cameras['vidCamera01']
obj.location = 0.032130539417266846, -8.493929862976074, 4.560103893280029
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.204706072807312, -0.0, 0.003782744985073805
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09494125843048096, -5.109508514404297, 3.929835319519043
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.0961123704910278, 4.656612873077393e-10, -0.018579155206680298
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(113 + frame)
obj = cameras['vidCamera01']
obj.location = 0.034126996994018555, -8.493499755859375, 4.571628570556641
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2035070657730103, -0.0, 0.004017990082502365
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09412498772144318, -5.2732744216918945, 3.8635647296905518
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.118933081626892, 4.656612873077393e-10, -0.017847545444965363
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(114 + frame)
obj = cameras['vidCamera01']
obj.location = 0.03582882881164551, -8.493132591247559, 4.581452369689941
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2024857997894287, -0.0, 0.004218538291752338
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09330140054225922, -5.426341533660889, 3.796093702316284
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.140287160873413, -0.0, -0.017192469909787178
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(115 + frame)
obj = cameras['vidCamera01']
obj.location = 0.03724569082260132, -8.492826461791992, 4.589631080627441
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2016360759735107, -0.0, 0.0043855165131390095
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0923268049955368, -5.563756942749023, 3.7140753269195557
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.162034273147583, -0.0, -0.016592808067798615
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(116 + frame)
obj = cameras['vidCamera01']
obj.location = 0.03838694095611572, -8.49258041381836, 4.596218585968018
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2009519338607788, 1.1641532182693481e-10, 0.004520023241639137
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09139151871204376, -5.69563102722168, 3.635364055633545
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1822841167449951, 4.6566123179658803e-10, -0.016044525429606438
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(117 + frame)
obj = cameras['vidCamera01']
obj.location = 0.039260685443878174, -8.492392539978027, 4.601262092590332
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2004284858703613, -1.1641532182693481e-10, 0.004623007029294968
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.09049042314291, -5.822684288024902, 3.559530258178711
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2012282609939575, -0.0, -0.01553976722061634
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(118 + frame)
obj = cameras['vidCamera01']
obj.location = 0.03987610340118408, -8.492259979248047, 4.604814529418945
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.2000598907470703, -0.0, 0.004695545881986618
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.08953657746315002, -5.939280033111572, 3.477381706237793
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.2199969291687012, 4.656612873077393e-10, -0.015074186027050018
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(119 + frame)
obj = cameras['vidCamera01']
obj.location = 0.040239691734313965, -8.492181777954102, 4.6069135665893555
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.199842095375061, 1.1641530794914701e-10, 0.004738402087241411
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0885390043258667, -6.046773433685303, 3.3899526596069336
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2386054992675781, -0.0, -0.014641311019659042
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(120 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.08757041394710541, -6.151144027709961, 3.305062770843506
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.256271481513977, 4.656612873077393e-10, -0.014235484413802624
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(121 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.08662833273410797, -6.252657890319824, 3.222496747970581
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.273076057434082, -2.3283064365386963e-10, -0.01385375764220953
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(122 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.08565878868103027, -6.344879627227783, 3.134937286376953
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.289846420288086, -0.0, -0.013499641790986061
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(123 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.08467496186494827, -6.429898262023926, 3.0442802906036377
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3064597845077515, -0.0, -0.013168185018002987
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(124 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.08371461927890778, -6.5128865242004395, 2.9557876586914062
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.322398066520691, -0.0, -0.012852982617914677
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(125 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.08277647942304611, -6.59395694732666, 2.869340419769287
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 1.3377017974853516, -0.0, -0.012552727945148945
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(126 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.08184481412172318, -6.668617248535156, 2.78104567527771
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3528028726577759, 2.3283064365386963e-10, -0.012272517196834087
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(127 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.08091293275356293, -6.735130310058594, 2.6893200874328613
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.3679178953170776, -2.3283064365386963e-10, -0.01201299112290144
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(128 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.08000119775533676, -6.800204753875732, 2.5995774269104004
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3825088739395142, -0.0, -0.011763987131416798
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(129 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07910895347595215, -6.863888263702393, 2.511753797531128
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3965970277786255, 2.3283064365386963e-10, -0.011524875648319721
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(130 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07823716849088669, -6.925028324127197, 2.4250404834747314
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.410280466079712, -1.1641533570472262e-10, -0.011297262273728848
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(131 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07739567011594772, -6.975447654724121, 2.3341708183288574
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4241442680358887, -1.1641532182693481e-10, -0.011094989255070686
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(132 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07657213509082794, -7.0247907638549805, 2.245241165161133
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.4375734329223633, 1.1641530794914701e-10, -0.010899843648076057
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(133 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07576637715101242, -7.073069095611572, 2.158231019973755
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4505776166915894, -1.1641530794914701e-10, -0.010711545124650002
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(134 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0749782994389534, -7.120287895202637, 2.0731301307678223
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4631646871566772, -0.0, -0.010529846884310246
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(135 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07425383478403091, -7.158658981323242, 1.986219882965088
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4757531881332397, -0.0, -0.010372220538556576
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(136 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07356157898902893, -7.193517684936523, 1.900064468383789
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4880931377410889, -0.0, -0.010225738398730755
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(137 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0728859230875969, -7.227541923522949, 1.8159751892089844
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5000463724136353, -5.8207653974573503e-11, -0.010084129869937897
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(138 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07222716510295868, -7.260714530944824, 1.7339887619018555
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.5116121768951416, -0.0, -0.009947339072823524
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(139 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07163223624229431, -7.288746356964111, 1.6527602672576904
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 1.5229512453079224, 2.9103826987286752e-11, -0.009827470406889915
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(140 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07112500071525574, -7.309468746185303, 1.571662187576294
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5341612100601196, 2.9103830456733704e-11, -0.009730224497616291
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(141 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07063297927379608, -7.3295698165893555, 1.4929966926574707
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.544983148574829, -2.9103833926180656e-11, -0.00963641982525587
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(142 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.07015696167945862, -7.349017143249512, 1.4168896675109863
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5554025173187256, -0.0, -0.009546153247356415
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(143 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06972020119428635, -7.366381645202637, 1.3432655334472656
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.565431833267212, -0.0, -0.009464365430176258
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(144 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06947217136621475, -7.372361660003662, 1.2707691192626953
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.575269103050232, -3.637978807091713e-12, -0.009423049166798592
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(145 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06923528760671616, -7.378073692321777, 1.2015280723571777
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5846490859985352, -0.0, -0.009383650496602058
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(146 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0690106675028801, -7.383489608764648, 1.1358733177185059
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5935276746749878, 1.4551915228366852e-11, -0.00934634916484356
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(147 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06879977881908417, -7.388575077056885, 1.0742321014404297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6018483638763428, -2.9103830456733704e-11, -0.009311377070844173
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(148 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06886597722768784, -7.380743503570557, 1.017709732055664
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6095296144485474, 2.9103826987286752e-11, -0.009330224245786667
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(149 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06895837187767029, -7.372093200683594, 0.9665622711181641
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.6165003776550293, 2.9103833926180656e-11, -0.009353703819215298
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(150 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06903920322656631, -7.3645243644714355, 0.921811580657959
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.62260901927948, -2.9103826987286752e-11, -0.009374292567372322
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(151 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06910552829504013, -7.358314037322998, 0.8850932121276855
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.6276277303695679, -5.820766785236131e-11, -0.009391214698553085
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(152 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.06915254890918732, -7.353911876678467, 0.8590660095214844
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6311886310577393, -0.0, -0.0094032296910882
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(153 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01972329616546631, -26.735923767089844, 14.102916717529297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1243127584457397, -0.0, 0.000737707014195621
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(154 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.014515519142150879, -27.32862091064453, 14.037670135498047
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1347533464431763, -0.0, 0.0005311465938575566
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(155 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.009907901287078857, -27.852996826171875, 13.979944229125977
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1437004804611206, -1.45519117589199e-11, 0.0003557206364348531
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(156 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.005770742893218994, -28.323854446411133, 13.928112030029297
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.151511549949646, -0.0, 0.0002037409140029922
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(157 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.002460479736328125, -28.72850227355957, 13.801506042480469
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1604609489440918, -0.0, 8.564542804379016e-05
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(158 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.00024646520614624023, -29.08272933959961, 13.626832962036133
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1700059175491333, 2.2737367544323206e-13, -8.475136382912751e-06
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(159 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.0027507543563842773, -29.410438537597656, 13.465234756469727
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1786985397338867, -0.0, -9.353037603432313e-05
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(160 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.005084037780761719, -29.71577262878418, 13.314672470092773
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.1866799592971802, 3.637979240772582e-12, -0.00017108935571741313
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(161 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.006936967372894287, -29.977428436279297, 13.139925003051758
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1947492361068726, -7.275957614183426e-12, -0.00023140685516409576
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(162 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.008164763450622559, -30.18593406677246, 12.923103332519531
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.2033518552780151, -0.0, -0.0002704828802961856
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(163 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.009327709674835205, -30.383405685424805, 12.717752456665039
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2114421129226685, -0.0, -0.0003070006496272981
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(164 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.010433793067932129, -30.571239471435547, 12.52242660522461
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2190855741500854, -0.0, -0.0003412949154153466
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(165 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.011489927768707275, -30.75060272216797, 12.335908889770508
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2263367176055908, -0.0, -0.0003736493526957929
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(166 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.012500107288360596, -30.922313690185547, 12.157051086425781
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.2332432270050049, -0.0, -0.00040424277540296316
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(167 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.012834250926971436, -31.034202575683594, 11.946537017822266
obj.scale = 1.0, 1.0, 1.0000001192092896
obj.rotation_euler = 1.2404271364212036, -1.4551915228366852e-11, -0.00041355230496264994
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(168 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.013156473636627197, -31.142086029052734, 11.743553161621094
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.2473384141921997, -0.0, -0.0004224665171932429
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(169 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.013467967510223389, -31.246395111083984, 11.547296524047852
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.2540056705474854, -0.0, -0.00043102516792714596
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(170 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.013769865036010742, -31.347503662109375, 11.35706615447998
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.260453462600708, -0.0, -0.0004392655973788351
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(171 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.01406317949295044, -31.44573211669922, 11.172249794006348
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.266703486442566, -0.0, -0.00044722104212269187
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(172 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.014348804950714111, -31.541370391845703, 10.992307662963867
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2727746963500977, -0.0, -0.00045492060598917305
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(173 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.014627397060394287, -31.634674072265625, 10.816761016845703
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.2786839008331299, -1.4551916963090328e-11, -0.00046238538925535977
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(174 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.01454317569732666, -31.694889068603516, 10.63245964050293
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.284550666809082, -0.0, -0.000458849681308493
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(175 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.014410734176635742, -31.749492645263672, 10.450231552124023
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.2903082370758057, -0.0, -0.0004538891080301255
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(176 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.014280855655670166, -31.80303955078125, 10.271533012390137
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2959535121917725, -0.0, -0.00044904107926413417
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(177 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.01415330171585083, -31.855632781982422, 10.096033096313477
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3014968633651733, 7.275957614183426e-12, -0.00044429555418901145
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(178 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.014027833938598633, -31.907352447509766, 9.923433303833008
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3069472312927246, -7.275957614183426e-12, -0.00043964313226751983
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(179 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.013904273509979248, -31.95828628540039, 9.753467559814453
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3123127222061157, -0.0, -0.0004350761300884187
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(180 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.01378244161605835, -32.00850296020508, 9.58588695526123
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.317601203918457, 7.275958481545164e-12, -0.0004305873590055853
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(181 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.013662219047546387, -32.05807113647461, 9.420473098754883
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3228192329406738, -0.0, -0.00042617146391421556
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(182 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.013543307781219482, -32.107051849365234, 9.257022857666016
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3279730081558228, -0.0, -0.00042181764729321003
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(183 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.013194739818572998, -32.13601303100586, 9.09093952178955
obj.scale = 1.0, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3330590724945068, -7.275958481545164e-12, -0.0004105909029021859
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(184 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.012813806533813477, -32.16166687011719, 8.925829887390137
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3380967378616333, -0.0, -0.00039841904072090983
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(185 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.012436389923095703, -32.18708801269531, 8.762219429016113
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3430925607681274, -0.0, -0.0003863786696456373
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(186 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.012062013149261475, -32.21229934692383, 8.599966049194336
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3480507135391235, -0.0, -0.0003744541318155825
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(187 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.011690497398376465, -32.2373161315918, 8.438936233520508
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.3529746532440186, -7.27595587945995e-12, -0.000362639082595706
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(188 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.011321544647216797, -32.26216506958008, 8.27900218963623
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3578683137893677, -0.0, -0.00035092374309897423
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(189 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.010954737663269043, -32.286865234375, 8.120054244995117
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3627345561981201, -0.0, -0.0003392944054212421
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(190 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.010590016841888428, -32.311424255371094, 7.961982250213623
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3675763607025146, -0.0, -0.00032774879946373403
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(191 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.01022714376449585, -32.33586120605469, 7.804691314697266
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.37239670753479, -0.0, -0.000316279154503718
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(192 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.009865820407867432, -32.36019515991211, 7.648090362548828
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3771978616714478, -3.637979240772582e-12, -0.0003048756916541606
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(193 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.009401679039001465, -32.376590728759766, 7.491264343261719
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.3819624185562134, -3.637979674453451e-12, -0.0002903855638578534
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(194 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.0088425874710083, -32.38566207885742, 7.334195137023926
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3866974115371704, -3.637979240772582e-12, -0.0002730406413320452
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(195 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.008285045623779297, -32.394710540771484, 7.177587509155273
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3914241790771484, -0.0, -0.0002557534899096936
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(196 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.0077288150787353516, -32.40373229980469, 7.0213727951049805
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 1.3961445093154907, -0.0, -0.00023851664445828646
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(197 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.007173895835876465, -32.41273880004883, 6.865488052368164
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.400860071182251, -0.0, -0.00022132997401058674
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(198 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.006619930267333984, -32.421730041503906, 6.709874153137207
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4055724143981934, -0.0, -0.00020418234635144472
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(199 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.006066739559173584, -32.43070602416992, 6.554476261138916
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.410283088684082, -0.0, -0.00018706823175307363
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(200 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.0055141448974609375, -32.439674377441406, 6.399243354797363
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4149932861328125, 1.818989620386291e-12, -0.00016998196952044964
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(201 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.0046710968017578125, -32.4533576965332, 6.162429332733154
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4221872091293335, 1.818989620386291e-12, -0.00014393309538718313
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(202 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.0038757920265197754, -32.46626281738281, 5.939042091369629
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4289820194244385, -0.0, -0.0001193795251310803
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(203 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.0029121041297912598, -32.46622848510742, 5.726217746734619
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.435412049293518, 9.094948101931455e-13, -8.969687041826546e-05
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(204 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.001950979232788086, -32.46389389038086, 5.522439002990723
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4415701627731323, -0.0, -6.00973580731079e-05
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(205 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.001026749610900879, -32.46165084838867, 5.326496601104736
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4475017786026, -0.0, -3.163007568218745e-05
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(206 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = -0.00013512372970581055, -32.4594841003418, 5.137454986572266
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4532334804534912, -0.0, -4.1633020373410545e-06
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(207 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.0007274150848388672, -32.457393646240234, 4.954592704772949
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.458785891532898, -0.0, 2.241092261101585e-05
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(208 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.001563429832458496, -32.45536422729492, 4.777349472045898
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4641751050949097, -0.0, 4.8171234084293246e-05
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(209 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.0023750662803649902, -32.453392028808594, 4.6052751541137695
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4694137573242188, -0.0, 7.318345160456374e-05
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(210 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.003164052963256836, -32.451480865478516, 4.438006401062012
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.474511981010437, -0.0, 9.750058234203607e-05
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(211 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.003994643688201904, -32.44715881347656, 4.275337219238281
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.479468584060669, -0.0, 0.00012311182217672467
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(212 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.004943490028381348, -32.437496185302734, 4.11712646484375
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4842804670333862, -0.0, 0.00015240002539940178
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(213 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.005867958068847656, -32.42808151245117, 3.9629709720611572
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4889756441116333, -0.0, 0.00018095252744387835
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(214 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.0067691802978515625, -32.41890335083008, 3.8127026557922363
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4935585260391235, -0.0, 0.0002088030450977385
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(215 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.007647871971130371, -32.40995407104492, 3.66617751121521
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.498032808303833, -1.8189894035458565e-12, 0.00023597247491125017
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(216 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.008504807949066162, -32.40122604370117, 3.5232815742492676
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.50240159034729, -0.0, 0.00026248369249515235
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(217 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.00934058427810669, -32.39271545410156, 3.3839163780212402
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.506667137145996, -0.0, 0.0002883540000766516
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(218 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01015561819076538, -32.38441467285156, 3.2480034828186035
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5108314752578735, -0.0, 0.0003135953738819808
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(219 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01095038652420044, -32.37632369995117, 3.115478277206421
obj.scale = 1.0, 1.0, 1.0000001192092896
obj.rotation_euler = 1.514896035194397, -0.0, 0.00033822160912677646
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(220 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.011725127696990967, -32.368431091308594, 2.9862897396087646
obj.scale = 1.0, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5188621282577515, -1.8189894035458565e-12, 0.0003622391086537391
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(221 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.012603998184204102, -32.35845184326172, 2.8605778217315674
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.522721290588379, -1.8189894035458565e-12, 0.0003895113186445087
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(222 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.013556957244873047, -32.34693908691406, 2.7382726669311523
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5264772176742554, -1.8189894035458565e-12, 0.00041911055450327694
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(223 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.014484643936157227, -32.335731506347656, 2.619210958480835
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.530137300491333, -0.0, 0.0004479450290091336
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(224 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.015387177467346191, -32.3248291015625, 2.5033841133117676
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 1.5337014198303223, -0.0, 0.00047601680853404105
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(225 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01626443862915039, -32.314231872558594, 2.390793800354004
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.537169098854065, 1.818989620386291e-12, 0.0005033207125961781
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(226 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.0171164870262146, -32.30393600463867, 2.2814486026763916
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5405398607254028, -1.818989620386291e-12, 0.0005298571195453405
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(227 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.01794302463531494, -32.29395294189453, 2.175365686416626
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5438127517700195, 9.094948101931455e-13, 0.0005556151154451072
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(228 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.018744051456451416, -32.28427505493164, 2.072568893432617
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.546986699104309, -9.094948101931455e-13, 0.0005805932451039553
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(229 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.019519150257110596, -32.2749137878418, 1.9730925559997559
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5500603914260864, 9.094947017729282e-13, 0.0006047772476449609
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(230 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.020268023014068604, -32.265865325927734, 1.8769760131835938
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.553032398223877, -9.09494593352711e-13, 0.0006281562964431942
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(231 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.021103620529174805, -32.25680923461914, 1.7843017578125
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5558996200561523, -0.0, 0.0006542371120303869
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(232 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.02211850881576538, -32.24748611450195, 1.6951539516448975
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.558659315109253, -0.0, 0.000685898179654032
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(233 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.023093342781066895, -32.23853302001953, 1.6095325946807861
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.5613114833831787, 4.547472966763555e-13, 0.0007163268164731562
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(234 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.024027109146118164, -32.22995376586914, 1.5275135040283203
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5638536214828491, 4.547472966763555e-13, 0.0007454893202520907
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(235 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.02491891384124756, -32.22175979614258, 1.4491796493530273
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.566282868385315, -2.2737362123312344e-13, 0.0007733560632914305
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(236 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.02576768398284912, -32.21396255493164, 1.3746237754821777
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.5685961246490479, 1.1368682416908887e-13, 0.000799891131464392
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(237 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.026572346687316895, -32.20656967163086, 1.3039488792419434
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5707900524139404, -0.0, 0.0008250592509284616
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(238 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.02733147144317627, -32.1995964050293, 1.2372698783874512
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.572860836982727, -1.1368683772161603e-13, 0.0008488134481012821
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(239 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.028043627738952637, -32.19305419921875, 1.1747145652770996
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.5748043060302734, -2.2737362123312344e-13, 0.0008711072732694447
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(240 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.028707265853881836, -32.18695831298828, 1.1164255142211914
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5766160488128662, -0.0, 0.0008918905514292419
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(241 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.029576241970062256, -32.18277359008789, 1.0624792575836182
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.578292965888977, -4.547473508864641e-13, 0.000919007754418999
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(242 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.030975162982940674, -32.182373046875, 1.012953281402588
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.579831838607788, -0.0, 0.0009624877129681408
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(243 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.03223836421966553, -32.182010650634766, 0.9682316780090332
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5812214612960815, -0.0, 0.0010017503518611193
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(244 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.03335970640182495, -32.18168640136719, 0.9285321235656738
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.582455039024353, 9.09494593352711e-13, 0.0010366045171394944
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(245 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.0343327522277832, -32.1814079284668, 0.8940830230712891
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5835254192352295, -0.0, 0.0010668496834114194
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(246 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.03515005111694336, -32.18117141723633, 0.865147590637207
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5844244956970215, -9.094947017729282e-13, 0.0010922541841864586
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(247 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.03580331802368164, -32.18098449707031, 0.8420193195343018
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.5851430892944336, 1.818989186705422e-12, 0.001112560392357409
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(248 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.03628337383270264, -32.18084716796875, 0.8250226974487305
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.585671305656433, -1.8189894035458565e-12, 0.0011274825083091855
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(249 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.03658008575439453, -32.18075942993164, 0.8145174980163574
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5859977006912231, -0.0, 0.001136705745011568
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(250 + frame)
obj = cameras['vidCamera01']
obj.location = 0.04035907983779907, -8.492155075073242, 4.607602596282959
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1997705698013306, -0.0, 0.004752475768327713
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = -0.0691714957356453, -7.352138042449951, 0.8485760688781738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.632624626159668, -0.0, -0.009408076293766499
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 120.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.0366818904876709, -32.18073272705078, 0.8109142780303955
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5861096382141113, -1.8189894035458565e-12, 0.0011398703791201115
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 98.0
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

