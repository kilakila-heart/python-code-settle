#--*coding:utf-8
import cv2 

import numpy as np

img = cv2.imread("xxx.gif")

#对于JPEG，其表示的是图像的质量，用0-100的整数表示，默认为95。
#注意，cv2.IMWRITE_JPEG_QUALITY类型为Long，必须转换成int
cv2.imwrite("666.gif", img, [int(cv2.IMWRITE_GIF_QUALITY), 65])
cv2.imwrite("6666.gif", img, [int(cv2.IMWRITE_GIF_QUALITY), 100])

cv2.waitKey (0)
cv2.destroyAllWindows()
