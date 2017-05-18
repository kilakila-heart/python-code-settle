#--*coding:utf-8
import cv2 

import numpy as np

img = cv2.imread("img//cat.jpg")
cv2.imshow(u'nature image',img)
#这是因为imshow()显示图像时对double/float型是认为在0~1范围内，
#即大于1时都是显示为白色，而imshow显示uint8型时是0~255范围。
cv2.imshow(u'become a white image',(img/1.0))
#除以256到1又变回来了
cv2.imshow(u'become back',(img/1.0)/256)
emptyImage = np.zeros(img.shape, np.uint8) #全0是黑色图像
whiteImage = 255*np.ones(img.shape, np.uint8) #全255是白色图像
cv2.imshow("whiteImage", whiteImage)
print whiteImage
print whiteImage.shape

emptyImage2 = img.copy()

emptyImage3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#emptyImage3[...]=0

cv2.imshow("EmptyImage", emptyImage)
cv2.imshow("Image", img)
cv2.imshow("EmptyImage2", emptyImage2)
cv2.imshow("EmptyImage3", emptyImage3)
#对于JPEG，其表示的是图像的质量，用0-100的整数表示，默认为95。
#注意，cv2.IMWRITE_JPEG_QUALITY类型为Long，必须转换成int
cv2.imwrite("img/cat2.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
cv2.imwrite("img//cat3.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
#对于PNG，第三个参数表示的是压缩级别。cv2.IMWRITE_PNG_COMPRESSION，
#从0到9,压缩级别越高，图像尺寸越小
cv2.imwrite("img/cat4.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
cv2.imwrite("img/cat5.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
cv2.waitKey (0)
cv2.destroyAllWindows()
