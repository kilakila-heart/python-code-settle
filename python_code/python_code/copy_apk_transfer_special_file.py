#-*- coding:utf-8-*-
import os
import shutil
#-*- coding:utf-8 -*-
import os
import shutil

def getFileName(path):
    ''' 获取指定目录下的所有指定后缀的文件名 '''

    f_list = os.listdir(path)
    # print f_list
    for i in f_list:
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1].find('apk'):
            print i
            return True


def filter_ext(args,dirn,fln):
    for fls in fln:
        if fls.lower().endswith(args[1].lower()):
            args[0].append(os.path.join(dirn,fls))

def cp_ext(ext,src=".",dest="."):
    if not os.path.exists(dest):
        v=raw_input("The target path doesn't exist,want going?[y]")
        if v in ['y','Y']:
            os.mkdir(dest)
        else:
            return False
    assert os.path.isdir(src) or os.path.isdir(dest),TypeError("ALL path must be Dir")
    assert os.path.exists(src),ValueError("Source Path Must exists!")
    ll=[]
    os.path.walk(src,filter_ext,(ll,ext))
    for l in ll:
        if os.path.isfile(l):
            print("Copying File:"+l)
            shutil.copy(l,dest)
if  __name__ == '__main__':
##    path = '/home/xx/work/ETS/log/1/1'
##    getFileName(path)
    getFileName('D:\\adst')
    cp_ext('apk',"D:\\adst","D:\\1")

'''python复制某文件夹下指定扩展名的文件，并且保留原目录结构

用法如下：
参考：http://outofmemory.cn/code-snippet/705/python-copy-mou-wenjianjia-
specify-kuozhanming-file-moreover-maintain-yuan-directory-structure

cp_tree_ext(exts,src,dest)

exts:以空格分隔的字符串，可多个拓展名，如"bat txt"
src:原目录
dest:目标目录，如果不存在，则建立'''
