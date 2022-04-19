# import os
# os.environ["OPENCV_IO_ENABLE_OPENEXR"] = "1"
# import cv2
import numpy
#
# img = cv2.imread('094_hdrmaps_com_free.exr', flags=cv2.IMREAD_ANYDEPTH)
# img1 = numpy.clip(numpy.power(img, 0.45), 0, 1)
# cv2.imshow('1', img1)
# cv2.waitKey(0)
# cv2.imwrite('test.jpg', img1)
import imageio
from PIL import Image
im = imageio.imread("094_hdrmaps_com_free.exr")
im_gamma_correct = numpy.clip(numpy.power(im, 0.50), 0, 1)
im_fixed = Image.fromarray(numpy.uint8(im_gamma_correct*255))
im_fixed.show()
im_fixed.save('test.jpg')


# import sys, os
# import imageio
#
# def convert_exr_to_jpg(exr_file, jpg_file):
#     if not os.path.isfile(exr_file):
#         return False
#
#     filename, extension = os.path.splitext(exr_file)
#     if not extension.lower().endswith('.exr'):
#         return False
#
#     # imageio.plugins.freeimage.download() #DOWNLOAD IT
#     image = imageio.imread(exr_file)
#     print(image.dtype)
#
#     # remove alpha channel for jpg conversion
#     image = image[:,:,:3]
#
#
#     data = 65535 * image
#     data[data>65535]=65535
#     rgb_image = data.astype('uint8')
#     print(rgb_image.dtype)
#     #rgb_image = imageio.core.image_as_uint(rgb_image, bitdepth=16)
#
#     imageio.imwrite(jpg_file, rgb_image, format='jpeg')
#     return True
#
#
# if __name__ == '__main__':
#     exr = "094_hdrmaps_com_free.exr"
#     jpg = "torus3.jpeg"
#     convert_exr_to_jpg(exr, jpg)
