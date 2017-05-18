#--*coding:utf-8 --*
def getDicFromFile(fileName):
    file1 = open(fileName)
    dic = {}
    for line in file1:
        dic = eval(line)
        return dic
if __name__ == '__main__':
    #用eval能够生成的字典本身已经构造成了字典的形式的字符串写入了文件中
    dic=getDicFromFile('yoochoose-buysRate-oneClick.dat')
    print isinstance(dic,dict)
