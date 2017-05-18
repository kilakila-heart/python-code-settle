#--*coding:utf-8
#生成和图像大小一样的背景图片
#这里有些颜色和RGB表不符
import cv2 
import numpy as np
img = cv2.imread("img\\cat.jpg")
img_blue=np.array([255,0,0])*np.ones(img.shape)
img_red=np.array([0,0,255])*np.ones(img.shape)
img_green=np.array([0,255,0])*np.ones(img.shape)
img_cyan=np.array([255,255,0])*np.ones(img.shape)
img_yellow=np.array([0,255,255])*np.ones(img.shape)
print img_red
##print img
##print img.shape #先高度后宽度(height,width,channel)
cv2.namedWindow("Image") 
cv2.imshow("Image", img)
cv2.imshow("Image_red", img_red)
cv2.imshow("Image_blue", img_blue)
cv2.imshow("Image_green", img_green)
cv2.imshow("Image_cyan", img_cyan)
cv2.imshow("Image_yellow", img_yellow)
cv2.waitKey (0)
cv2.destroyAllWindows()
