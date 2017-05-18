# -*- coding: cp936 -*-
import string
import math
def getPopularItem():#得到popularItem的字典
    file_object1 = open('D:\Data\yoochoose-buys-analyse-sorted.dat')
    number = 0
    for line in file_object1:
        number += string.atoi(line.split("\t")[1])
    threadNumber = number * 9/10
    number = 0
    s={}
    file_object1 = open('D:\Data\yoochoose-buys-analyse-sorted.dat')
    for line in file_object1:
        number += string.atoi(line.split("\t")[1])
        if number > threadNumber :
            break
        else:
            s[line.split("\t")[0]] = 1
    return s
def getDicFromFile(fileName):
    file1 = open(fileName)
    dic = {}
    for line in file1:
        dic = eval(line)
    return dic
def getpopularItem_feature_valify():
    itemPrice={}
    buysession=getDicFromFile("D:\\Data\\yoochoose-buys-info.dat")
    s=getPopularItem()
    popularNumber=0
    i=0
    buypopularNumber=0
    file_clicks=open("D:\\Data\\yoochoose-clicks.dat")
    itemPrice=getDicFromFile("D:\\Data\\yoochoose-buys-itemPrice.dat")
    for line in file_clicks:
        i+=1
        data=line.split(",")
        if i%100000==0:
            print i
        if s.has_key(data[2]):#如果属于流行项目
            popularNumber+=1
            if itemPrice.has_key(data[2]):#如果属于购买项目
                buypopularNumber+=1
                
    print  str(buypopularNumber), str(popularNumber),str(buypopularNumber/popularNumber)        
getpopularItem_feature_valify()
    

