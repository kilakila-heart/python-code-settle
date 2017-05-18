#--*coding:utf-8 --*
import Image  
img = Image.open("16.png") 
 
for i in xrange(512):
    for j in xrange(512):
        
        r,g,b = img.getpixel((i,j))
        if(g > b and r > g): #对蓝色进行判断
            b=127
            g=127
            r=127
         
        img.putpixel((i,j), (r,g,b)) 
 
img.show()
