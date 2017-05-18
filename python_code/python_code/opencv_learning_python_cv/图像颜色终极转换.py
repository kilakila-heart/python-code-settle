#--*coding:utf-8 --*
#参考：http://blog.csdn.net/icamera0/article/details/50785776
from PIL import Image,ImageOps
im02 = Image.open("16.png")  
im = ImageOps.autocontrast(im02, 20)  
r,g,b = im02.split()  
print r.mode  
im_r = ImageOps.colorize(r, "green", "blue")  
im_b = ImageOps.colorize(b, (255, 0, 0), (0, 255, 0))  
im_g = ImageOps.colorize(g, (255, 0, 0), "blue")
im_r.save("imrr.png")
im_b.save("imb.png")
im_g.save("img.png")
