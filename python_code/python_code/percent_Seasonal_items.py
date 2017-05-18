# ---*coding:cp936 --*
import string
import math
def percent_Seasonal_items():
#�б���Ŀ��Ӧ��ʱ�Ĺ�����ռ��Ŀ�ܵĹ������ı������Ӷ�̽����Ŀ��Ӧ���Զ���Ŀ�����۵�Ӱ��
    file_buy=open('D:\Data\yoochoose-buys.dat')
    buysFrequentness = getBuysFrequentness('D:\Data\yoochoose-buys-analyse-sorted.dat')
    #buy����Ŀ���乺��������ֵ�
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
def getBuysFrequentness(buyFile): #buyFileָD:\Data\yoochoose-buys-analyse-sorted.dat
#buy-analyse-sorted.dat�洢����buy�е���Ŀ���������
    buysFrequentnessFile = open(buyFile)#buysFrequentnessFile�洢����buy�е���Ŀ:����������ֵ�
    buysFrequentness = {}
    for line in buysFrequentnessFile:
        data = line.split("\t")
        buysFrequentness[data[0]] = string.atoi(data[1])
    return buysFrequentness
percent_Seasonal_items()
