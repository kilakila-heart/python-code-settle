#--*coding:cp936--*
# -*- coding: cp936 -*-

import os

path = 'E:\\LearningToCount_ver1_01\\data1'

for file in os.listdir(path):

    if os.path.isfile(os.path.join(path,file))==True:
        print( file)

##        if file.match(:
##
##            newname=file+'rsfdjndk.jpg'
##
##            os.rename(os.path.join(path,file),os.path.join(path,newname))
##
##            print file,'ok'
##    #        print file.split('.')[-1]
