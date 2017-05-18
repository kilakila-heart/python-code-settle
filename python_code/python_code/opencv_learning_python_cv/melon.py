#--*coding:utf-8
#生成和图像大小一样的背景图片
#这里有些颜色和RGB表不符
import cv2 
import numpy as np
img = cv2.imread("img\\melon.jpg")

print img.ndim
print img.shape
print img
cv2.namedWindow("Image") 
cv2.imshow("Image", img)

cv2.waitKey (0)
cv2.destroyAllWindows()
