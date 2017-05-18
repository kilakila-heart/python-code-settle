#--*coding:utf-8 --*
# 文件自动备份脚本
import os
import shutil
# 设置待备份的源文件夹及存放备份文件的目标文件夹
srcDir = "D:\pdf"
dstDir = "D:\\adst"
# 目录递归拷贝函数
# 目录递归拷贝函数
def dir_copyTree(src, dst):
    names = os.listdir(src)
    # 目标文件夹不存在，则新建
    if not os.path.exists(dst):
        os.mkdir(dst)
    
    # 遍历源文件夹中的文件与文件夹
    for name in names:
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            # 是文件夹则递归调用本拷贝函数，否则直接拷贝文件
            if os.path.isdir(srcname):
                dir_copyTree(srcname, dstname)
            else:
                if dst.endswith('dist') and dstname.endswith('apk'):
                    if (not os.path.exists(dstname)
                        or ((os.path.exists(dstname))
                            and (os.path.getsize(dstname) != os.path.getsize(srcname)))):
                        print dstname
                        shutil.copy2(srcname, dst)
        except:
            error.traceback();
            raise
# 备份函数
def dir_backup():
    global srcDir
    global dstDir
    print "源文件夹" + srcDir
    print "目标文件夹" + dstDir
    print "本次拷贝文件："
    dir_copyTree(srcDir, dstDir)
    # 将此句注释则会一闪而过，方便自动备份
    raw_input ("备份完成,点enter确认")
# 执行备份函数
dir_backup()
###########################################################################
