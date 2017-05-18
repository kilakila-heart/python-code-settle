#!/usr/bin/python
#--*coding:utf-8 --*
import sys,os

def fileCountIn(dir):
    return sum([len(files) for root,dirs,files in os.walk(dir)])

#得益于Python精髓的列表解析，所以一句话就搞定了
#os.walk(dir)会返回一个三元组：（当前目录，子目录列表，文件列表）
#所以len(files)就是获取当前目录下的文件数，然后每个目录下的文件数求和即可
fileCountIn('D:\Bag_Of_Words_Recent\CODE_!___Linear Spatial Pyramid Matching Using Sparse Coding\matlab_toolbox-master\CVPR09-ScSPM\data')
#函数返回9144
