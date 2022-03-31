import bpy

font_curve = bpy.data.curves.new(type="FONT", name="Font Curve")
font_curve.body = "菜逼一群"
font_obj = bpy.data.objects.new(name="Font Object", object_data=font_curve)
bpy.context.scene.collection.objects.link(font_obj)
font_file = bpy.data.fonts.load(filepath=r"C:\WINDOWS\Fonts\simhei.ttf")
font_curve.font = font_file
font_curve.resolution_u = 12  # U向预览分辨率
font_curve.render_resolution_u = 12  # U向渲染分辨率
font_curve.use_auto_texspace = True  # 自动纹理空间
font_curve.offset = 0.15  # 几何数据 偏移量
font_curve.extrude = 0.2  # 几何数据 挤出
font_curve.bevel_depth = 0.08  # 倒角深度
font_curve.bevel_resolution = 4 # 倒角分辨率
font_curve.align_x = 'CENTER'  # 段 水平居中
font_curve.align_y = 'CENTER'  # 段 垂直居中
font_curve.space_character = 4.2  # 字符间隔
font_curve.space_word = 0  # 单词间隔
font_curve.space_line = 0  # 行间隔
