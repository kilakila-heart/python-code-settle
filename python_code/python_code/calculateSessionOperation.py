# --*coding:cp936 --*
import math
import string
def calculateSessionOperation(inFile,outFile):
    #calculateItemOperation('D:\Data\yoochoose-clicks-hasBuyData.dat',
    #'D:\Data\yoochoose-hasbuydata_Session-analyse-sorted.dat')
    #calculateItemOperation('D:\Data\yoochoose-buys.dat',
    #'D:\Data\yoochoose-buys_Session-analyse-sorted.dat')
    file_object = open(inFile)
    file_object_w = open(outFile, 'w')
    s = {}
    a={}
    i=1
    number = 0
    ItemFrequency=getDicFromFile('D:\Data\yoochoose-buys-analyse-sorted.dat')
    buySessionFre=getDicFromFile('D:\Data\yoochoose-buy-Session-frequency.dat')
    for line in file_object:
        
        if number%100000 ==0:
            print number
        number+=1    
        index = line.split(",")[0]
        item=line.split(",")[2]
        if s.has_key(index):
            i+=1                    #hasbuydata中某次会话的出现数
            if  s[index]==None:
                s[index]=0
            if  ItemFrequency.has_key(item):
                if  s[index]<ItemFrequency[item]:
                    s[index]=ItemFrequency[item]
        else:
             i=1
             if  ItemFrequency.has_key(item):
                s[index]=ItemFrequency[item]             
        a[index]=i
    s = sorted(s.iteritems(),key=lambda s:s[1],reverse=True)
    file_object_w.write("Session"+"\t"+"maxItemBuyfrequency"+"\t"+"buySession/hasbuySession"+"\n")
    for line in s:       
  #      file_object_w.write(line[0]+ "\t"+str(line[1])+"\t"+str(1.0*buySessionFre[line[0]]/a[line[0]])+"\n")
         file_object_w.write(str(line[1])+"\t"+str(1.0*buySessionFre[line[0]])+"\n")
    file_object_w.close()
    
def getDicFromFile(fileName):#项目及其次数的字典
    file1 = open(fileName)
    dic = {}        #{string:Integer}
    for line in file1:
        dic[line.split("\t")[0]] =string.atoi(line.split("\t")[1],10)
    return dic
calculateSessionOperation('D:\Data\yoochoose-clicks-hasBuyData.dat',
                          'D:\Data\yoochoose-BuyRateForMaxFrequency_of_Item2.dat')
