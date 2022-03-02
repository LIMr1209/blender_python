import bpy
import os

# 渲染图片的一部分
# cut final image into 10 by 10 smaller images
cut_into = 10
# location of folder to save images to
output_folder = '//renders'

rndr = bpy.context.scene.render

rndr.use_border = True
rndr.use_crop_to_border = False

for row in range(cut_into):
    for column in range(cut_into):
        filename = "chunk_{}_{}".format(row + 1, column + 1)
        rndr.filepath = os.path.join(output_folder, filename)

        rndr.border_min_x = (1 / cut_into) * row
        rndr.border_max_x = (1 / cut_into) * (row + 1)
        rndr.border_min_y = (1 / cut_into) * column
        rndr.border_max_y = (1 / cut_into) * (column + 1)

        bpy.ops.render.render(write_still=True)
