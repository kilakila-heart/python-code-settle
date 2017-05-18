#coding:--utf-8--*

import shutil
import os
import os.path
srcDir = "J:\pdf"
dstDir = "D:\\adst"
def dir_copy_apk(src, dst):
    for root, dirs, files in os.walk(src):
        for name in files:
            srcname = os.path.join(src, name)
            dstname = os.path.join(dst, name)
            if name.find(".apk") and name.find("dist"):
                if (not os.path.exists(dstname)):
                    print root+'/'+name
                    shutil.copy2(name, dst)
# 备份函数
def dir_backup():
    global srcDir
    print "源文件夹" + srcDir
    print "目标文件夹" + dstDir
    print "本次拷贝文件："
    dir_copy_apk(srcDir, dstDir)
dir_backup()
    # 将此句注释则会一闪而过，方便自动备份
##def getFileName(path):
##    ''' 获取指定目录下的所有指定后缀的文件名 '''
##
##    f_list = os.listdir(path)
##    # print f_list
##    for i in f_list:
##        # os.path.splitext():分离文件名与扩展名
##        if os.path.splitext(i)[1].strip() == '.apk':
##            print i
##
##
##if __name__ == '__main__':
##
##    path = 'D:\\adst'
##    getFileName(path)
