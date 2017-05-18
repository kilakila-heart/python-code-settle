#--*coding:utf-8 --*
#参考：http://www.cnblogs.com/ma6174/archive/2012/05/04/2482378.html
import os
path = 'D:\image\Caltech101'
j=0

for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        if file.find('.png')>0: 
            newname=str(j)+'.png'            
            os.rename(os.path.join(path,file),os.path.join(path,newname))
            print file,'ok'
            j+=1
