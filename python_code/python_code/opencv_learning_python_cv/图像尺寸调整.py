import cv2
filename="ic_launcher.png"
image=cv2.imread(filename)
res=cv2.resize(image,(512,512),interpolation=cv2.INTER_CUBIC)
cv2.imshow('iker',res)
cv2.imshow('image',image)
cv2.imwrite(filename,res)
cv2.waitKey(0)
cv2.destoryAllWindows()
