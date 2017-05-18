# ---*coding:cp936 --*
import string
import math
def percent_Seasonal_items():
#判别项目在应季时的购买量占项目总的购买量的比例，从而探查项目的应季性对项目的销售的影响
    file_buy=open('D:\Data\yoochoose-buys.dat')
    buysFrequentness = getBuysFrequentness('D:\Data\yoochoose-buys-analyse-sorted.dat')
    #buy中项目与其购买次数的字典
    file_percent_Seasonal_items=open('D:\Data\yoochoose-buys-percentOfSeasonal_items.dat','w')
    buyMaxMonth = getDicFromFile('D:\Data\yoochoose-buyMaxMonth.dat')
    s={}
    for line in  file_buy:
        data=line.split(",")
        month=line.split("-")[1]
        if month==buyMaxMonth[data[2]]:
            if s.has_key(data[2]):
                s[data[2]]+=1
            else:
                s[data[2]]=1
    file_percent_Seasonal_items.write("item"+"\t"+"buy_in_maxMonth"+"\t"+"buyAll"
                                               +"\t"+"buy_in_maxMonth/buyAll"+"\n")
    for item in s:
      if buysFrequentness.has_key(item):             
        file_percent_Seasonal_items.write(item+"\t"+str(s[item])+"\t"+str(buysFrequentness[item])+
                                          "\t"+str(1.0*s[item]/buysFrequentness[item])+"\n")
    file_percent_Seasonal_items.close()
def getDicFromFile(fileName):
    file1 = open(fileName)
    dic = {}
    for line in file1:
        dic = eval(line)
        return dic
def getBuysFrequentness(buyFile): #buyFile指D:\Data\yoochoose-buys-analyse-sorted.dat
#buy-analyse-sorted.dat存储的是buy中的项目即购买次数
    buysFrequentnessFile = open(buyFile)#buysFrequentnessFile存储的是buy中的项目:购买次数的字典
    buysFrequentness = {}
    for line in buysFrequentnessFile:
        data = line.split("\t")
        buysFrequentness[data[0]] = string.atoi(data[1])
    return buysFrequentness
percent_Seasonal_items()
