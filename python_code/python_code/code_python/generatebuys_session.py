#coding:utf-8 --*
#这段代码是为了生成存储字典的文件
def generateBuysSession(buysFile,outputFile):
    #yoochoose-buys.dat的文件形式
    #generateBuysSession('D:\Data\yoochoose-buys.dat','D:\Data\yoochoose-buys-info.dat')
    buysInfo = {}
    file_buys = open(buysFile)
    for session in file_buys:
        data = session.split(",")
        buysInfo[data[0]] = 1
    file_buys_info = open(outputFile,'w')
    #写的时候可以直接将字典写入文件，然后又可以直接用eval读取
    file_buys_info.write(str(buysInfo))
    file_buys_info.close()
if __name__=='__main__':
    generateBuysSession('yoochoose-buys.dat','yoochoose-buys-info.dat')
