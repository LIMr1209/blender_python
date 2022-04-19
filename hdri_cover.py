import os

os.environ["OPENCV_IO_ENABLE_OPENEXR"] = "1"

import cv2

img = cv2.imread('094_hdrmaps_com_free.exr', flags=cv2.IMREAD_ANYDEPTH)
cv2.imshow('1', img)
cv2.waitKey(0)
cv2.imwrite('test.jpg', img)
# import imageio
# imageio.plugins.freeimage.download()
# img = imageio.imread('094_hdrmaps_com_free.exr', format='HDR-FI')