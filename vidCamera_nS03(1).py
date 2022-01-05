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
obj.location = -8.685591697692871, -6.728650093078613, 7.696243762969971
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.0374479293823242, -0.0, -0.9116793870925903
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(31 + frame)
obj = cameras['vidCamera01']
obj.location = -8.684820175170898, -6.73043155670166, 7.6950531005859375
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.0375473499298096, -0.0, -0.9115081429481506
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(32 + frame)
obj = cameras['vidCamera01']
obj.location = -8.682443618774414, -6.7359161376953125, 7.691385746002197
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.0378539562225342, -0.0, -0.9109811186790466
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(33 + frame)
obj = cameras['vidCamera01']
obj.location = -8.678365707397461, -6.745327949523926, 7.685092926025391
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0
obj.rotation_euler = 1.03838050365448, -0.0, -0.9100772142410278
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(34 + frame)
obj = cameras['vidCamera01']
obj.location = -8.672479629516602, -6.758910179138184, 7.676011562347412
obj.scale = 1.000000238418579, 1.0, 1.0
obj.rotation_euler = 1.0391409397125244, -1.4901161193847656e-08, -0.9087734222412109
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(35 + frame)
obj = cameras['vidCamera01']
obj.location = -8.66466999053955, -6.7769317626953125, 7.663961410522461
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.040151596069336, -0.0, -0.9070447087287903
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(36 + frame)
obj = cameras['vidCamera01']
obj.location = -8.654809951782227, -6.799686431884766, 7.648747444152832
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0
obj.rotation_euler = 1.0414297580718994, -0.0, -0.9048643708229065
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(37 + frame)
obj = cameras['vidCamera01']
obj.location = -8.642759323120117, -6.827495574951172, 7.630153179168701
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.0429952144622803, 1.4901161193847656e-08, -0.9022030234336853
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(38 + frame)
obj = cameras['vidCamera01']
obj.location = -8.628363609313965, -6.860714912414551, 7.607941627502441
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.0448702573776245, -0.0, -0.8990288972854614
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(39 + frame)
obj = cameras['vidCamera01']
obj.location = -8.611372947692871, -6.89969539642334, 7.581844806671143
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0
obj.rotation_euler = 1.0470763444900513, -0.0, -0.8953053951263428
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(40 + frame)
obj = cameras['vidCamera01']
obj.location = -8.590494155883789, -6.944317817687988, 7.551488876342773
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.0496000051498413, 1.4901160305669237e-08, -0.8909712433815002
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(41 + frame)
obj = cameras['vidCamera01']
obj.location = -8.56651782989502, -6.995562553405762, 7.516627788543701
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.0525104999542236, -1.4901161193847656e-08, -0.8860049843788147
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(42 + frame)
obj = cameras['vidCamera01']
obj.location = -8.539194107055664, -7.053957939147949, 7.476902484893799
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.0558428764343262, -1.4901161193847656e-08, -0.8803609013557434
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(43 + frame)
obj = cameras['vidCamera01']
obj.location = -8.50825023651123, -7.120092391967773, 7.431913375854492
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.0596367120742798, -0.0, -0.8739887475967407
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(44 + frame)
obj = cameras['vidCamera01']
obj.location = -8.473379135131836, -7.194619178771973, 7.381213188171387
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.0639369487762451, -1.4901161193847656e-08, -0.8668336868286133
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(45 + frame)
obj = cameras['vidCamera01']
obj.location = -8.434237480163574, -7.278273582458496, 7.324305057525635
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.0687941312789917, -0.0, -0.8588355183601379
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(46 + frame)
obj = cameras['vidCamera01']
obj.location = -8.389896392822266, -7.371583938598633, 7.260598182678223
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.0742452144622803, 2.980232594040899e-08, -0.8499162197113037
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(47 + frame)
obj = cameras['vidCamera01']
obj.location = -8.337193489074707, -7.4740142822265625, 7.189307689666748
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.0802555084228516, -0.0, -0.8399368524551392
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(48 + frame)
obj = cameras['vidCamera01']
obj.location = -8.278493881225586, -7.588100433349609, 7.109904766082764
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.0870070457458496, -0.0, -0.8288831114768982
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(49 + frame)
obj = cameras['vidCamera01']
obj.location = -8.213220596313477, -7.714962005615234, 7.021611213684082
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.094581961631775, -1.4901159417490817e-08, -0.8166695833206177
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(50 + frame)
obj = cameras['vidCamera01']
obj.location = -8.140737533569336, -7.8558349609375, 6.923564434051514
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.103071928024292, -1.4901161193847656e-08, -0.8032065033912659
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(51 + frame)
obj = cameras['vidCamera01']
obj.location = -8.060345649719238, -8.012080192565918, 6.814818859100342
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.11257803440094, 1.4901161193847656e-08, -0.788401186466217
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(52 + frame)
obj = cameras['vidCamera01']
obj.location = -7.964839935302734, -8.18148136138916, 6.694106101989746
obj.scale = 1.0, 1.0, 1.0
obj.rotation_euler = 1.1229835748672485, -2.980232594040899e-08, -0.7719815373420715
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(53 + frame)
obj = cameras['vidCamera01']
obj.location = -7.857667922973633, -8.368006706237793, 6.560512542724609
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.1345691680908203, -0.0, -0.7539559602737427
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(54 + frame)
obj = cameras['vidCamera01']
obj.location = -7.7393293380737305, -8.57396411895752, 6.413000583648682
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1475034952163696, 1.4901161193847656e-08, -0.7342798709869385
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(55 + frame)
obj = cameras['vidCamera01']
obj.location = -7.609000205993652, -8.800788879394531, 6.250542640686035
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.1618976593017578, -0.0, -0.7128987312316895
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(56 + frame)
obj = cameras['vidCamera01']
obj.location = -7.456817626953125, -9.043949127197266, 6.0721845626831055
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0
obj.rotation_euler = 1.177539348602295, -0.0, -0.689507782459259
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(57 + frame)
obj = cameras['vidCamera01']
obj.location = -7.285422325134277, -9.306014060974121, 5.877471923828125
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1946172714233398, -0.0, -0.66420978307724
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(58 + frame)
obj = cameras['vidCamera01']
obj.location = -7.099765300750732, -9.589884757995605, 5.666557312011719
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2132898569107056, -0.0, -0.6372893452644348
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(59 + frame)
obj = cameras['vidCamera01']
obj.location = -6.895604133605957, -9.890812873840332, 5.440494537353516
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.2332943677902222, -0.0, -0.6088258624076843
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(60 + frame)
obj = cameras['vidCamera01']
obj.location = -6.661650657653809, -10.197137832641602, 5.201571464538574
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.2540621757507324, -0.0, -0.5786819458007812
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(61 + frame)
obj = cameras['vidCamera01']
obj.location = -6.417746543884277, -10.516490936279297, 4.952487468719482
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2758275270462036, 7.450580596923828e-09, -0.5479261875152588
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(62 + frame)
obj = cameras['vidCamera01']
obj.location = -6.162487983703613, -10.839519500732422, 4.697656631469727
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.2980009317398071, -0.0, -0.5169510245323181
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(63 + frame)
obj = cameras['vidCamera01']
obj.location = -5.880216598510742, -11.144691467285156, 4.443056106567383
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3195838928222656, 7.450580596923828e-09, -0.4855025112628937
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(64 + frame)
obj = cameras['vidCamera01']
obj.location = -5.601068496704102, -11.44648551940918, 4.1912736892700195
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.3409273624420166, -0.0, -0.45507240295410156
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(65 + frame)
obj = cameras['vidCamera01']
obj.location = -5.325305461883545, -11.736684799194336, 3.9466910362243652
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3615097999572754, -7.450580596923828e-09, -0.42595288157463074
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(66 + frame)
obj = cameras['vidCamera01']
obj.location = -5.028951644897461, -11.986794471740723, 3.7161219120025635
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3802841901779175, -0.0, -0.39723777770996094
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(67 + frame)
obj = cameras['vidCamera01']
obj.location = -4.746954917907715, -12.224788665771484, 3.49672269821167
obj.scale = 1.000000238418579, 1.0, 1.0
obj.rotation_euler = 1.3981053829193115, -0.0, -0.3703845739364624
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(68 + frame)
obj = cameras['vidCamera01']
obj.location = -4.480588912963867, -12.449588775634766, 3.289484977722168
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.4148527383804321, 3.725290298461914e-09, -0.345465749502182
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(69 + frame)
obj = cameras['vidCamera01']
obj.location = -4.207142353057861, -12.634424209594727, 3.1007490158081055
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4296987056732178, -0.0, -0.3214418590068817
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(70 + frame)
obj = cameras['vidCamera01']
obj.location = -3.9394237995147705, -12.79434585571289, 2.9269628524780273
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4431829452514648, -3.725290076417309e-09, -0.29869183897972107
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(71 + frame)
obj = cameras['vidCamera01']
obj.location = -3.6891021728515625, -12.94387435913086, 2.764469861984253
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4557572603225708, -1.862645371275562e-09, -0.27764615416526794
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(72 + frame)
obj = cameras['vidCamera01']
obj.location = -3.455256462097168, -13.083562850952148, 2.6126718521118164
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4674557447433472, -0.0, -0.25819656252861023
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(73 + frame)
obj = cameras['vidCamera01']
obj.location = -3.2255859375, -13.196392059326172, 2.4763171672821045
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4777954816818237, 1.862645149230957e-09, -0.2397288829088211
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(74 + frame)
obj = cameras['vidCamera01']
obj.location = -2.994089365005493, -13.275278091430664, 2.3570873737335205
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4866502285003662, -0.0, -0.22182714939117432
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(75 + frame)
obj = cameras['vidCamera01']
obj.location = -2.777709484100342, -13.34901237487793, 2.245643138885498
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4949325323104858, -9.313225746154785e-10, -0.20515593886375427
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(76 + frame)
obj = cameras['vidCamera01']
obj.location = -2.5753161907196045, -13.417981147766113, 2.141402244567871
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.5026772022247314, -1.862645371275562e-09, -0.18962426483631134
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(77 + frame)
obj = cameras['vidCamera01']
obj.location = -2.385861396789551, -13.482540130615234, 2.043825626373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5099185705184937, -0.0, -0.17514614760875702
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(78 + frame)
obj = cameras['vidCamera01']
obj.location = -2.208373546600342, -13.543022155761719, 1.9524123668670654
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.516690731048584, 9.31322685637781e-10, -0.161640927195549
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(79 + frame)
obj = cameras['vidCamera01']
obj.location = -2.031888246536255, -13.572935104370117, 1.8773128986358643
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.5221573114395142, 4.656613428188905e-10, -0.14859797060489655
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(80 + frame)
obj = cameras['vidCamera01']
obj.location = -1.8604880571365356, -13.585550308227539, 1.8129665851593018
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.526797890663147, -4.6566123179658803e-10, -0.13609948754310608
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(81 + frame)
obj = cameras['vidCamera01']
obj.location = -1.6995532512664795, -13.597395896911621, 1.752549171447754
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5311698913574219, -0.0, -0.12434621900320053
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(82 + frame)
obj = cameras['vidCamera01']
obj.location = -1.548354148864746, -13.608524322509766, 1.6957868337631226
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5352884531021118, 4.656612873077393e-10, -0.11329106986522675
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(83 + frame)
obj = cameras['vidCamera01']
obj.location = -1.4062235355377197, -13.61898422241211, 1.6424288749694824
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5391684770584106, -0.0, -0.1028900220990181
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(84 + frame)
obj = cameras['vidCamera01']
obj.location = -1.2725601196289062, -13.628822326660156, 1.5922496318817139
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5428235530853271, -0.0, -0.09310276806354523
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(85 + frame)
obj = cameras['vidCamera01']
obj.location = -1.1468119621276855, -13.638078689575195, 1.5450419187545776
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5462665557861328, -0.0, -0.0838916078209877
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(86 + frame)
obj = cameras['vidCamera01']
obj.location = -1.02848219871521, -13.646787643432617, 1.5006191730499268
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5495095252990723, -0.0, -0.0752222090959549
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(87 + frame)
obj = cameras['vidCamera01']
obj.location = -0.9171135425567627, -13.654984474182129, 1.458809733390808
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5525637865066528, -0.0, -0.06706256419420242
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(88 + frame)
obj = cameras['vidCamera01']
obj.location = -0.8109033107757568, -13.645822525024414, 1.4278103113174438
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.5548096895217896, 5.8207653974573503e-11, -0.05935521423816681
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(89 + frame)
obj = cameras['vidCamera01']
obj.location = -0.7099509239196777, -13.62514877319336, 1.4045991897583008
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5564796924591064, -5.820766091346741e-11, -0.05205884203314781
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(90 + frame)
obj = cameras['vidCamera01']
obj.location = -0.6149518489837646, -13.605693817138672, 1.3827569484710693
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5580579042434692, -0.0, -0.04516739025712013
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(91 + frame)
obj = cameras['vidCamera01']
obj.location = -0.5255725383758545, -13.587389945983887, 1.3622066974639893
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5595483779907227, -0.0, -0.03866163268685341
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(92 + frame)
obj = cameras['vidCamera01']
obj.location = -0.44151973724365234, -13.57017707824707, 1.342881202697754
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5609548091888428, -0.0, -0.032524559646844864
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(93 + frame)
obj = cameras['vidCamera01']
obj.location = -0.36250758171081543, -13.553995132446289, 1.3247146606445312
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5622811317443848, 1.4551915228366852e-11, -0.02673906646668911
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(94 + frame)
obj = cameras['vidCamera01']
obj.location = -0.2882859706878662, -13.538795471191406, 1.3076494932174683
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5635305643081665, -1.4551913493643376e-11, -0.021290108561515808
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(95 + frame)
obj = cameras['vidCamera01']
obj.location = -0.21861481666564941, -13.524528503417969, 1.291630744934082
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5647063255310059, 7.275957614183426e-12, -0.016162915155291557
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(96 + frame)
obj = cameras['vidCamera01']
obj.location = -0.1532728672027588, -13.511146545410156, 1.2766071557998657
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5658117532730103, -0.0, -0.011343693360686302
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(97 + frame)
obj = cameras['vidCamera01']
obj.location = -0.0920562744140625, -13.49860954284668, 1.262532114982605
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.5668495893478394, -1.818989186705422e-12, -0.006819580681622028
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(98 + frame)
obj = cameras['vidCamera01']
obj.location = -0.034776926040649414, -13.486879348754883, 1.2493624687194824
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5678225755691528, 9.094947017729282e-13, -0.0025785700418055058
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(99 + frame)
obj = cameras['vidCamera01']
obj.location = 0.018739938735961914, -13.475919723510742, 1.2370578050613403
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5687332153320312, -0.0, 0.0013906221138313413
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(100 + frame)
obj = cameras['vidCamera01']
obj.location = 0.06866741180419922, -13.46569538116455, 1.2255784273147583
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5695841312408447, -0.0, 0.005099387373775244
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(101 + frame)
obj = cameras['vidCamera01']
obj.location = 0.11515092849731445, -13.456175804138184, 1.2148908376693726
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.5703775882720947, 2.2737367544323206e-13, 0.008557267487049103
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(102 + frame)
obj = cameras['vidCamera01']
obj.location = 0.1583387851715088, -13.447331428527832, 1.2049609422683716
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5711156129837036, 2.2737367544323206e-13, 0.011774190701544285
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(103 + frame)
obj = cameras['vidCamera01']
obj.location = 0.1983654499053955, -13.43913459777832, 1.1957581043243408
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5718005895614624, 9.09494593352711e-13, 0.014759210869669914
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(104 + frame)
obj = cameras['vidCamera01']
obj.location = 0.23535871505737305, -13.431558609008789, 1.1872527599334717
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.5724341869354248, 1.818989186705422e-12, 0.017521020025014877
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(105 + frame)
obj = cameras['vidCamera01']
obj.location = 0.2694394588470459, -13.424579620361328, 1.1794167757034302
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5730185508728027, -0.0, 0.020067911595106125
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1408335268497467, -2.0527782440185547, 5.928920745849609
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.4966835677623749, 0.07942187041044235, -0.16350948810577393
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.633853554725647, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(106 + frame)
obj = cameras['vidCamera01']
obj.location = 0.30071425437927246, -13.418174743652344, 1.172226071357727
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.505773663520813, -0.0, 0.02240721508860588
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.1424168050289154, -2.1158745288848877, 5.930134296417236
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 0.4613289535045624, 0.07264360040426254, -0.16619530320167542
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(107 + frame)
obj = cameras['vidCamera01']
obj.location = 0.3292877674102783, -13.412322998046875, 1.1656564474105835
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5062363147735596, 1.1641532182693481e-10, 0.02454620786011219
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.4249167740345001, -2.8252475261688232, 5.854545593261719
obj.scale = 1.0000001192092896, 0.9999999403953552, 1.0
obj.rotation_euler = 0.5778709053993225, 0.09457194805145264, -0.0635177493095398
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(108 + frame)
obj = cameras['vidCamera01']
obj.location = 0.35526347160339355, -13.407003402709961, 1.1596840620040894
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.506657361984253, -0.0, 0.026492152363061905
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 0.7591062784194946, -3.181922435760498, 5.653761863708496
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 0.6508846282958984, 0.10763521492481232, 0.03272410109639168
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(109 + frame)
obj = cameras['vidCamera01']
obj.location = 0.3787357807159424, -13.402196884155273, 1.1542872190475464
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5070384740829468, 1.1641532182693481e-10, 0.028251711279153824
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 1.057207703590393, -3.4329745769500732, 5.4541544914245605
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 0.710689902305603, 0.11788807064294815, 0.10644429922103882
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(110 + frame)
obj = cameras['vidCamera01']
obj.location = 0.39979100227355957, -13.397884368896484, 1.1494461297988892
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.5073806047439575, -0.0, 0.02983100898563862
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 1.3300085067749023, -3.6267507076263428, 5.260209560394287
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 0.7634432315826416, 0.12656669318675995, 0.1673741340637207
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(111 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4185149669647217, -13.394049644470215, 1.1451411247253418
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5076851844787598, -0.0, 0.03123617358505726
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 1.5809921026229858, -3.7862863540649414, 5.075046539306641
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 0.8115593791007996, 0.13416317105293274, 0.219040185213089
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(112 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4349839687347412, -13.390677452087402, 1.1413547992706299
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5079532861709595, -0.0, 0.032472673803567886
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 1.8173298835754395, -3.9181630611419678, 4.894596099853516
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 0.8562498688697815, 0.14093096554279327, 0.2649962604045868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(113 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4492766857147217, -13.387750625610352, 1.1380685567855835
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5081862211227417, -2.3283061589829401e-10, 0.03354619815945625
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 2.0377509593963623, -4.044708251953125, 4.728226184844971
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 0.8987690806388855, 0.1471007764339447, 0.30445757508277893
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(114 + frame)
obj = cameras['vidCamera01']
obj.location = 0.46146082878112793, -13.385254859924316, 1.135266900062561
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5083848237991333, -0.0, 0.03446166589856148
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 2.250105619430542, -4.141894340515137, 4.558259010314941
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 0.9385284781455994, 0.15262340009212494, 0.34212857484817505
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(115 + frame)
obj = cameras['vidCamera01']
obj.location = 0.471604585647583, -13.383177757263184, 1.1329346895217896
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5085502862930298, -0.0, 0.03522403910756111
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 2.452785015106201, -4.232841968536377, 4.396047115325928
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 0.9766514897346497, 0.15768738090991974, 0.3762456178665161
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(116 + frame)
obj = cameras['vidCamera01']
obj.location = 0.47977471351623535, -13.38150405883789, 1.131056308746338
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.508683681488037, -0.0, 0.03583822026848793
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 2.647001266479492, -4.322352886199951, 4.242519378662109
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.0133240222930908, 0.16233877837657928, 0.4070267081260681
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(117 + frame)
obj = cameras['vidCamera01']
obj.location = 0.48603081703186035, -13.380223274230957, 1.1296178102493286
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5087857246398926, 2.3283061589829401e-10, 0.03630860522389412
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 2.8346638679504395, -4.39782190322876, 4.0895304679870605
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.0483053922653198, 0.1665695607662201, 0.43636173009872437
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(118 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4904358386993408, -13.379321098327637, 1.1286051273345947
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5088577270507812, -2.3283064365386963e-10, 0.036639850586652756
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 3.0165886878967285, -4.46047306060791, 3.936800479888916
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.0818462371826172, 0.170432910323143, 0.4645663797855377
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(119 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4930393695831299, -13.378787994384766, 1.1280064582824707
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089002847671509, 2.3283064365386963e-10, 0.036835648119449615
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 3.1931674480438232, -4.523067951202393, 3.7902512550354004
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.114273190498352, 0.17398463189601898, 0.49066492915153503
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(120 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 3.365128517150879, -4.585663318634033, 3.6491527557373047
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.1455851793289185, 0.17724008858203888, 0.5149169564247131
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(121 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 3.5320491790771484, -4.6363935470581055, 3.507286787033081
obj.scale = 1.0, 1.0, 1.0000001192092896
obj.rotation_euler = 1.1756545305252075, 0.1802029013633728, 0.5385818481445312
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(122 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 3.694244384765625, -4.675593376159668, 3.364469528198242
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.204640507698059, 0.1829051822423935, 0.561817467212677
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(123 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 3.8530681133270264, -4.715320587158203, 3.2260053157806396
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2327197790145874, 0.18537725508213043, 0.5837015509605408
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(124 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 4.008845806121826, -4.755519866943359, 3.091494083404541
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.2598868608474731, 0.1876310259103775, 0.6043517589569092
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(125 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 4.161832809448242, -4.796128749847412, 2.9605965614318848
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.2861403226852417, 0.18967881798744202, 0.6238692998886108
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(126 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 4.308078765869141, -4.815919876098633, 2.824500560760498
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.3114269971847534, 0.19152911007404327, 0.6439904570579529
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(127 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 4.451304912567139, -4.833737850189209, 2.6907520294189453
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3359464406967163, 0.1932079941034317, 0.6633464694023132
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(128 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 4.592191219329834, -4.852258682250977, 2.5602407455444336
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.3597079515457153, 0.1947258710861206, 0.681784987449646
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(129 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 4.7308454513549805, -4.871402263641357, 2.4327688217163086
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.3827072381973267, 0.19609223306179047, 0.6993597745895386
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(130 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 4.867344379425049, -4.891085624694824, 2.3081719875335693
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4049433469772339, 0.1973164677619934, 0.7161187529563904
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(131 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 4.996167182922363, -4.893077850341797, 2.1804559230804443
obj.scale = 1.000000238418579, 1.0, 1.0
obj.rotation_euler = 1.4264203310012817, 0.19840818643569946, 0.7333694696426392
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(132 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 5.120814323425293, -4.888976573944092, 2.05342173576355
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4472484588623047, 0.19938135147094727, 0.7503743171691895
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(133 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 5.243444919586182, -4.885738849639893, 1.9292645454406738
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.467435598373413, 0.20024386048316956, 0.7666773200035095
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(134 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 5.364060401916504, -4.883285999298096, 1.8079065084457397
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4869753122329712, 0.2010028064250946, 0.7823036313056946
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(135 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 5.482638359069824, -4.8815484046936035, 1.6892971992492676
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.505861520767212, 0.20166517794132233, 0.7972757816314697
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(136 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 5.599117279052734, -4.880422115325928, 1.5734026432037354
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.524090051651001, 0.20223794877529144, 0.8116157054901123
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(137 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 5.702192783355713, -4.853649616241455, 1.4543856382369995
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.5416605472564697, 0.2027280479669571, 0.8269867300987244
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(138 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 5.803218841552734, -4.828094482421875, 1.3384108543395996
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5586680173873901, 0.2031443864107132, 0.8417629599571228
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(139 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 5.902101516723633, -4.803715229034424, 1.225520133972168
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.575095772743225, 0.2034922093153, 0.8559483289718628
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(140 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 5.998724937438965, -4.780474662780762, 1.115785002708435
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.590927004814148, 0.20377682149410248, 0.8695443868637085
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(141 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.0929365158081055, -4.758346080780029, 1.0093128681182861
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.606143593788147, 0.2040034830570221, 0.8825498223304749
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(142 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.184552192687988, -4.737307548522949, 0.9062522053718567
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.620725393295288, 0.20417766273021698, 0.894960343837738
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(143 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.26611852645874, -4.704766750335693, 0.8055775761604309
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.6345771551132202, 0.20430395007133484, 0.9074631929397583
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(144 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.337556838989258, -4.6612091064453125, 0.7076780796051025
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.6477316617965698, 0.20438861846923828, 0.9200578927993774
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(145 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.4061079025268555, -4.6199140548706055, 0.6141965985298157
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6602377891540527, 0.2044372409582138, 0.9319958090782166
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(146 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.47140645980835, -4.581027984619141, 0.5255622267723083
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.672037959098816, 0.20445460081100464, 0.943230390548706
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(147 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.532982349395752, -4.5447492599487305, 0.4423398971557617
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6830599308013916, 0.20444577932357788, 0.9537012577056885
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(148 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.590216636657715, -4.511361122131348, 0.365292489528656
obj.scale = 1.0, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6932092905044556, 0.20441634953022003, 0.9633257389068604
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(149 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.642275810241699, -4.481264114379883, 0.2954631447792053
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.702358365058899, 0.20437219738960266, 0.9719889163970947
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(150 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.687982082366943, -4.455048561096191, 0.23434686660766602
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.7103248834609985, 0.2043202966451645, 0.9795234799385071
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(151 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.725594520568848, -4.43361759185791, 0.1841849684715271
obj.scale = 1.0000001192092896, 1.0, 1.000000238418579
obj.rotation_euler = 1.7168331146240234, 0.2042684257030487, 0.9856733679771423
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(152 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5089142322540283, -2.3283064365386963e-10, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.752317428588867, -4.418469429016113, 0.14861774444580078
obj.scale = 1.0, 1.0000001192092896, 1.0
obj.rotation_euler = 1.7214306592941284, 0.2042268067598343, 0.9900151491165161
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5526865720748901, -0.0, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(153 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.650394439697266, 3.5024328231811523, 0.501349925994873
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6600086688995361, -1.862645149230957e-09, 1.8885107040405273
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(154 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.984076499938965, 1.9328298568725586, 0.574559211730957
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6539602279663086, -0.0, 1.7449796199798584
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(155 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.27929401397705, 0.5441570281982422, 0.6393299102783203
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.6472371816635132, 2.3283064365386963e-10, 1.6190028190612793
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(156 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.544380187988281, -0.7027826309204102, 0.6974897384643555
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.6404348611831665, -0.0, 1.5099947452545166
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(157 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.720946311950684, -1.844557762145996, 0.7731437683105469
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6323333978652954, 9.313225746154785e-10, 1.4147037267684937
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(158 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.832940101623535, -2.899017333984375, 0.8603029251098633
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6236010789871216, -0.0, 1.3305332660675049
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(159 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.936551094055176, -3.8745527267456055, 0.9409379959106445
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.6156502962112427, -0.0, 1.2569302320480347
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(160 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 12.033087730407715, -4.783466339111328, 1.016066312789917
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.6084764003753662, 9.313225746154785e-10, 1.1924244165420532
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(161 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 12.12358570098877, -5.635527610778809, 1.0864951610565186
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.6020307540893555, 9.31322685637781e-10, 1.1356701850891113
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(162 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 12.15339469909668, -6.4402618408203125, 1.1687088012695312
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.595184326171875, 9.31322685637781e-10, 1.083504319190979
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(163 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 12.159345626831055, -7.203071594238281, 1.2529296875
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.588575005531311, -0.0, 1.0359914302825928
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(164 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 12.165006637573242, -7.92864465713501, 1.3330390453338623
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.582584261894226, -0.0, 0.9931859374046326
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(165 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 12.170412063598633, -8.621498107910156, 1.4095358848571777
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5771443843841553, -2.3283061589829401e-10, 0.9544562101364136
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(166 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 12.175592422485352, -9.285449981689453, 1.482841968536377
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5721921920776367, -5.8207657444020455e-11, 0.9192619919776917
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(167 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 12.180572509765625, -9.92376708984375, 1.5533175468444824
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5676711797714233, -1.1641533570472262e-10, 0.8871434926986694
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(168 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 12.17245864868164, -10.538435935974121, 1.6239185333251953
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5633617639541626, 2.3283064365386963e-10, 0.8572232127189636
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(169 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 12.121834754943848, -11.130023956298828, 1.7009427547454834
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0
obj.rotation_euler = 1.5588425397872925, -0.0, 0.8280274271965027
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(170 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 12.072766304016113, -11.703445434570312, 1.7756016254425049
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5546576976776123, -0.0, 0.8009301424026489
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(171 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 12.025094032287598, -12.26054573059082, 1.8481354713439941
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5507726669311523, -0.0, 0.7757033705711365
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(172 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.978678703308105, -12.802953720092773, 1.9187564849853516
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.5471572875976562, 9.313225746154785e-10, 0.7521488666534424
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(173 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.93339729309082, -13.332113265991211, 1.9876525402069092
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5437843799591064, -9.313225746154785e-10, 0.7300938963890076
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(174 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.889141082763672, -13.84929370880127, 2.0549888610839844
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5406303405761719, 1.862645371275562e-09, 0.7093880772590637
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(175 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.84581184387207, -14.3556489944458, 2.1209158897399902
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.000000238418579
obj.rotation_euler = 1.537674069404602, -0.0, 0.6898995637893677
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(176 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.793841361999512, -14.850813865661621, 2.18660044670105
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5348291397094727, 1.862645149230957e-09, 0.6711664795875549
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(177 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.708696365356445, -15.332145690917969, 2.2548317909240723
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5319072008132935, -0.0, 0.6521925926208496
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(178 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.624959945678711, -15.805519104003906, 2.3219351768493652
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.529143214225769, -0.0, 0.634156346321106
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(179 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.542498588562012, -16.27167320251465, 2.3880155086517334
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.526524305343628, -0.0, 0.6169812679290771
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(180 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.461196899414062, -16.731285095214844, 2.4531679153442383
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5240389108657837, -1.862645149230957e-09, 0.6005986332893372
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(181 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.380945205688477, -17.184953689575195, 2.5174779891967773
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5216766595840454, 1.8626449271863521e-09, 0.5849471688270569
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(182 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.301645278930664, -17.633237838745117, 2.5810248851776123
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5194282531738281, 1.8626450382086546e-09, 0.5699716210365295
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(183 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.223209381103516, -18.076642990112305, 2.6438798904418945
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5172852277755737, -0.0, 0.5556224584579468
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(184 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.14555549621582, -18.515625, 2.706108331680298
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5152397155761719, -0.0, 0.5418550372123718
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(185 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 11.060482025146484, -18.94881820678711, 2.7677249908447266
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5132722854614258, -0.0, 0.5283501744270325
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(186 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.946428298950195, -19.371826171875, 2.8286619186401367
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5113426446914673, -0.0, 0.5143392086029053
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(187 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.833234786987305, -19.79164695739746, 2.889139175415039
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5094918012619019, -1.862645149230957e-09, 0.5008171200752258
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(188 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.720812797546387, -20.20861053466797, 2.949204921722412
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.5077147483825684, -0.0, 0.4877544641494751
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(189 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.60908317565918, -20.623003005981445, 3.0089006423950195
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.506007194519043, -1.862645371275562e-09, 0.4751245379447937
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(190 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.497968673706055, -21.035110473632812, 3.0682668685913086
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5043649673461914, 1.8626449271863521e-09, 0.46290239691734314
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(191 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.38740348815918, -21.44518280029297, 3.127340316772461
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.502784252166748, -0.0, 0.45106562972068787
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(192 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.277323722839355, -21.853456497192383, 3.186154365539551
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.501261591911316, -0.0, 0.43959322571754456
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(193 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.167671203613281, -22.260143280029297, 3.244739532470703
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4997938871383667, 1.862645149230957e-09, 0.4284660816192627
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(194 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 10.058389663696289, -22.66545867919922, 3.3031275272369385
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4983779191970825, -0.0, 0.41766613721847534
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(195 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 9.915013313293457, -23.059314727783203, 3.3564236164093018
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.497138500213623, 1.8626450382086546e-09, 0.406080037355423
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(196 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 9.77046012878418, -23.45172119140625, 3.4093661308288574
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4959471225738525, -0.0, 0.39475148916244507
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(197 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 9.626211166381836, -23.84330177307129, 3.4621968269348145
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4947960376739502, -0.0, 0.3837161362171173
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(198 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 9.482213973999023, -24.234203338623047, 3.5149359703063965
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4936832189559937, -0.0, 0.3729614019393921
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(199 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 9.338418006896973, -24.624557495117188, 3.567601442337036
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4926069974899292, -1.862645371275562e-09, 0.3624756336212158
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(200 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 9.194771766662598, -25.014501571655273, 3.620211601257324
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4915657043457031, -0.0, 0.35224759578704834
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(201 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 8.97563648223877, -25.609371185302734, 3.700469732284546
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4900394678115845, -1.862645149230957e-09, 0.33710455894470215
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(202 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 8.768625259399414, -26.170398712158203, 3.776085615158081
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.488668441772461, -1.862645149230957e-09, 0.3233027458190918
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(203 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 8.5215482711792, -26.684852600097656, 3.832719326019287
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4878631830215454, 1.8626449271863521e-09, 0.30910441279411316
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(204 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 8.285036087036133, -27.17731475830078, 3.886932134628296
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4871294498443604, 1.862645149230957e-09, 0.29590144753456116
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(205 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 8.057618141174316, -27.650833129882812, 3.9390597343444824
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4864565134048462, -1.862645371275562e-09, 0.2835538387298584
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(206 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 7.8382086753845215, -28.10767936706543, 3.989351749420166
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4858360290527344, 1.862645149230957e-09, 0.27195459604263306
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(207 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 7.625972270965576, -28.549591064453125, 4.037999629974365
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4852614402770996, -3.7252898543727042e-09, 0.26101920008659363
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(208 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 7.420257091522217, -28.977922439575195, 4.085152626037598
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4847277402877808, -0.0, 0.25067949295043945
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(209 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 7.206273555755615, -29.38656997680664, 4.123826026916504
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4844337701797485, -0.0, 0.24047797918319702
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(210 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 6.969696998596191, -29.769393920898438, 4.147191524505615
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.484566569328308, -1.8626449271863521e-09, 0.22998060286045074
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(211 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 6.739497184753418, -30.141897201538086, 4.16992712020874
obj.scale = 1.000000238418579, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.4847021102905273, 1.8626450382086546e-09, 0.21997421979904175
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(212 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 6.5153279304504395, -30.50464630126953, 4.192067623138428
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4848393201828003, -0.0, 0.2104230672121048
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(213 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 6.296903610229492, -30.85809326171875, 4.213640213012695
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.4849778413772583, -0.0, 0.2012963891029358
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(214 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 6.083987236022949, -31.202632904052734, 4.234668731689453
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.485116958618164, 1.862645149230957e-09, 0.19256702065467834
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(215 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 5.876374244689941, -31.538589477539062, 4.255173683166504
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4852561950683594, -0.0, 0.18421097099781036
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(216 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 5.673905372619629, -31.86621856689453, 4.27517032623291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4853951930999756, -0.0, 0.1762073040008545
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(217 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 5.44180154800415, -32.16164016723633, 4.269184112548828
obj.scale = 1.0000001192092896, 1.000000238418579, 1.0000001192092896
obj.rotation_euler = 1.4862322807312012, 9.313224635931761e-10, 0.16761410236358643
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(218 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 5.211329460144043, -32.44688034057617, 4.260316371917725
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.487125039100647, 9.313224635931761e-10, 0.15925106406211853
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(219 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 4.9866042137146, -32.725006103515625, 4.251669883728027
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4879883527755737, 9.31322685637781e-10, 0.1512157917022705
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(220 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 4.76753568649292, -32.996131896972656, 4.243240833282471
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4888231754302979, -0.0, 0.14349466562271118
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(221 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 4.55405855178833, -33.260337829589844, 4.235027313232422
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.489629864692688, -9.31322685637781e-10, 0.1360754370689392
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(222 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 4.346131801605225, -33.51767349243164, 4.22702693939209
obj.scale = 1.000000238418579, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.490409255027771, -0.0, 0.1289474070072174
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(223 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 4.143718242645264, -33.768184661865234, 4.219238758087158
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.4911619424819946, -0.0, 0.12210030853748322
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(224 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 3.946803331375122, -34.01189422607422, 4.211662292480469
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.491888165473938, -0.0, 0.11552516371011734
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(225 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 3.726351499557495, -34.2175407409668, 4.1729302406311035
obj.scale = 1.000000238418579, 1.0, 1.0
obj.rotation_euler = 1.4934170246124268, -0.0, 0.10847432911396027
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(226 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 3.5079896450042725, -34.41267013549805, 4.130709171295166
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.495011806488037, -0.0, 0.10158798098564148
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(227 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 3.2961456775665283, -34.60197448730469, 4.089748382568359
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.4965476989746094, -0.0, 0.09497232735157013
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(228 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 3.0908617973327637, -34.78541946411133, 4.050055980682373
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.4980252981185913, -0.0, 0.08862234652042389
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(229 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 2.892207622528076, -34.96294021606445, 4.011645317077637
obj.scale = 1.000000238418579, 1.0, 1.0
obj.rotation_euler = 1.4994450807571411, -0.0, 0.08253417164087296
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(230 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 2.7002627849578857, -35.134464263916016, 3.974532127380371
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.500807285308838, -9.313225746154785e-10, 0.07670431584119797
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(231 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 2.515125036239624, -35.299903869628906, 3.938735008239746
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5021122694015503, -4.656612873077393e-10, 0.07112999260425568
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(232 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 2.3369104862213135, -35.45915985107422, 3.9042763710021973
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5033600330352783, -0.0, 0.06580911576747894
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(233 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 2.165742874145508, -35.61211395263672, 3.871180534362793
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.504550814628601, 4.656613428188905e-10, 0.060739971697330475
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(234 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 1.983773946762085, -35.71982192993164, 3.806208848953247
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5065382719039917, 2.3283064365386963e-10, 0.05548006668686867
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(235 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 1.807499885559082, -35.81733703613281, 3.739569664001465
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5085463523864746, -0.0, 0.050421614199876785
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(236 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 1.639728307723999, -35.91014862060547, 3.67614483833313
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5104503631591797, -0.0, 0.04563027620315552
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(237 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 1.4806907176971436, -35.99812698364258, 3.6160218715667725
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5122486352920532, 2.3283064365386963e-10, 0.04110925644636154
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(238 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 1.3306407928466797, -36.08113479614258, 3.5592966079711914
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5139391422271729, -0.0, 0.03686242550611496
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(239 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 1.1898729801177979, -36.15900421142578, 3.506080389022827
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5155198574066162, -0.0, 0.032894816249608994
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(240 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 1.0587046146392822, -36.2315673828125, 3.4564931392669678
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5169880390167236, 1.1641532182693481e-10, 0.029212191700935364
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(241 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.9374837279319763, -36.29862594604492, 3.4106667041778564
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5183407068252563, -1.1641533570472262e-10, 0.02582123503088951
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(242 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.8266004920005798, -36.35996627807617, 3.3687479496002197
obj.scale = 1.000000238418579, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5195746421813965, -1.1641532182693481e-10, 0.022729890421032906
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(243 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.7264732718467712, -36.41535949707031, 3.3308956623077393
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5206859111785889, -0.0, 0.0199469905346632
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(244 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.6375865340232849, -36.46453094482422, 3.297292709350586
obj.scale = 1.0000001192092896, 1.0, 1.0000001192092896
obj.rotation_euler = 1.5216702222824097, -5.820766091346741e-11, 0.017483333125710487
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(245 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.5604605078697205, -36.507198333740234, 3.2681357860565186
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5225225687026978, 5.820766785236131e-11, 0.015350849367678165
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(246 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.4956781268119812, -36.543033599853516, 3.243645191192627
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5232371091842651, -0.0, 0.013563398271799088
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(247 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.44389504194259644, -36.571678161621094, 3.224069118499756
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.5238075256347656, -0.0, 0.012137075886130333
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(248 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.4058406949043274, -36.59273147583008, 3.2096829414367676
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.524226188659668, -0.0, 0.011090290732681751
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(249 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.38231974840164185, -36.605743408203125, 3.2007908821105957
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5244847536087036, -0.0, 0.01044387649744749
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 135.0
data.keyframe_insert('lens')

# new frame
scene.frame_set(250 + frame)
obj = cameras['vidCamera01']
obj.location = 0.4938938617706299, -13.378612518310547, 1.127810001373291
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0000001192092896
obj.rotation_euler = 1.5989047288894653, -0.0, 0.03689991682767868
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera02']
obj.location = 6.710997104644775, -4.3775529861450195, 0.3426787853240967
obj.scale = 1.0000001192092896, 1.0, 1.0
obj.rotation_euler = 1.849662184715271, 0.20137716829776764, 1.0172475576400757
obj.keyframe_insert('location')
obj.keyframe_insert('scale')
obj.keyframe_insert('rotation_euler')
data = obj.data
data.lens = 50.0
data.keyframe_insert('lens')

obj = cameras['vidCamera03']
obj.location = 0.37425440549850464, -36.610206604003906, 3.197741985321045
obj.scale = 1.0000001192092896, 1.0000001192092896, 1.0
obj.rotation_euler = 1.5245734453201294, -0.0, 0.01022232323884964
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

