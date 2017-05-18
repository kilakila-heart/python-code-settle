#coding:cp936 --*
import os.path
import pprint
import os
import os.path
'''
    os.walk这个某块是遍历一个目录常用的模块，它返回一个包含3个元素的元祖:dirpath,dirnames,filenames.
    dirpath是以string字符串形式返回该目录下所有的绝对路径；
    dirnames是以列表list形式返回每一个绝对路径下的文件夹名字；
    filesnames是以列表list形式返回该路径下所有文件名字。
'''
filename="E://paper"
for root, dirs, files in os.walk(filename):
    #print dirs
    for name in files:
        print(root) #----该目录下所有的绝对路径；
        print name
