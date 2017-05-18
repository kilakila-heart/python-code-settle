# -*- coding: cp936 -*-
import string
import math
import numpy as np
import matplotlib.pyplot as plt
#每个月第一天是星期几
monthWeekDay={4:1,
       5:3,
       6:6,
       7:1,
       8:5,
       9:1}
def getPopularItem():
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
def calculateTime(start,end):
    startData = start.split(":")
    startHour = string.atoi(startData[0].split("T")[1])
    startMinute = string.atoi(startData[1])
    endData = end.split(":")
    endHour = string.atoi(endData[0].split("T")[1])
    endMinute = string.atoi(endData[1])
    if startHour>endHour:
        endHour += 24
    return (endHour-startHour)*60+(endMinute-startMinute)

def calculateWeekTime(time): #计算属于星期几
    data = time.split("-")
    day = string.atoi(data[2].split("T")[0])
    return ((day-1)+monthWeekDay[string.atoi(data[1])])%7
def getPriceGrade(price,minPrice,maxPrice):
    return int(math.log10(price+1))
    #gradeInteval = (maxPrice-minPrice)/5+1
    #return (price-minPrice)/gradeInteval
def getMostGrade(clickInfo,itemPrice,minPrice,maxPrice):
    mostGrade = {}
    grade = -1
    for info in clickInfo:
        if itemPrice.has_key(info):
            grade = getPriceGrade(itemPrice[info],minPrice,maxPrice)
            if mostGrade.has_key(grade):
                mostGrade[grade] +=1
            else :
                mostGrade[grade] =1
    if mostGrade=={}:
        return -1
    mostGrade = sorted(mostGrade.iteritems(),key=lambda s:s[1],reverse=True)
    for grade in mostGrade:
        return grade[0]
#计算是否有重复点击，并返回价格区间
def repeatOrNot(clickInfo,itemPrice,minPrice,maxPrice,buysFrequentness):
    clickInfo1 = sorted(clickInfo.iteritems(),key=lambda s:s[1],reverse=True)
    maxBuysFrequentness = 0
    grade = -1
    for info in clickInfo1:
        if info[1]>1:
            if itemPrice.has_key(info[0]):
                grade =  getPriceGrade(itemPrice[info[0]],minPrice,maxPrice)
            else:
                grade = -1 #表示缺失
        else:
            grade = getMostGrade(clickInfo,itemPrice,minPrice,maxPrice)
        break
    repeatNumber = 0
    for info in clickInfo:
        if clickInfo[info]>1:
            if buysFrequentness.has_key(info):
                if buysFrequentness[info]> maxBuysFrequentness:
                    maxBuysFrequentness = buysFrequentness[info]
            repeatNumber+=1
    return repeatNumber,grade,maxBuysFrequentness

def generateCategoryValue():
    file_category = open('D:\Data\yoochoose-category.dat','w')
    file_click = open('D:\Data\yoochoose-clicks.dat')
    category = {}
    for line in file_click:
        data = line.split(",")
        categoryId = data[3].strip()
        if len(categoryId)>3:
            categoryId = '-1C'
        else:
            categoryId = categoryId+"C"
        category[data[2]] = categoryId
    file_category.write(str(category))
    file_category.close()

    
def getCategoryValue(categoryInfo):
    if len(categoryInfo)==0:
        return "0C"
    categoryInfo = sorted(categoryInfo.iteritems(),key=lambda s:s[1],reverse=True)
    return categoryInfo[0][0]

#获得商品价格
def getItemPrice():
    file_buys = open('D:\Data\yoochoose-buys.dat')
    maxPrice = 0
    minPrice = 10000000
    itemPrice = {}
    for line in file_buys:
        data = line.split(",")
        itemId = data[2]
        price = string.atoi(data[3])
        if price>0:
            if itemPrice.has_key(itemId):
                if price>itemPrice[itemId]:
                    itemPrice[itemId] = price
            else:
                itemPrice[itemId] = price
        if price>maxPrice:
            maxPrice = price
        if price<minPrice:
            minPrice = price
    return itemPrice,minPrice,maxPrice
def getBuysFrequentness(buyFile):
    buysFrequentnessFile = open(buyFile)
    buysFrequentness = {}
    for line in buysFrequentnessFile:
        data = line.split("\t")
        buysFrequentness[data[0]] = string.atoi(data[1])
    return buysFrequentness
def getDicFromFile(fileName):
    file1 = open(fileName)
    dic = {}
    for line in file1:
        dic = eval(line)
        return dic
#获得购买点击的特征
def getBuysFeature(fileOut,buyThreshold):
    file_buys = open('D:\Data\yoochoose-clicks-hasBuyData.dat')
    file_buys_out = open(fileOut,"w")
    file_buys_out.write("clickNumber,popularOrNot,repeatClick,priceGrade,categoryValue,buysFrequentness,month,category\n")
    itemPrice,minPrice,maxPrice = getItemPrice()
    popularItem = getPopularItem()
    buysFrequentness = getBuysFrequentness('D:\Data\yoochoose-buys-analyse-sorted.dat')
    buyMaxMonth = getDicFromFile('D:\Data\yoochoose-buyMaxMonth.dat')
    buyMonthLen = getDicFromFile('D:\Data\yoochoose-buyMonthLen.dat')
    beginTime = "-1"
    endTime = "-1"
    sessionId = "-1"
    clickInfo = {}
    categoryInfo={}
    category = {}
    file_category = open('D:\Data\yoochoose-category.dat')
    for line in file_category:
        category = eval(line)
        break
    clickNumber = 0
    popularOrNot = 0
    for line in file_buys:
        data = line.split(",")
        if sessionId != data[0]:
            if sessionId == "-1":
                beginTime = data[1]
                endTime = data[1]
                sessionId = data[0]
            else:
                if clickNumber==1:
                    time = 0
                else :
                    time = calculateTime(beginTime,endTime)
                weekTime = calculateWeekTime(endTime)
                categoryValue = getCategoryValue(categoryInfo)
                repeat,priceGrade,maxBuysFrequentness = repeatOrNot(clickInfo,itemPrice,minPrice,maxPrice,buysFrequentness)
                month = data[1].split("-")[1]
                monthRight = -1
                if buyMaxMonth.has_key(data[2]):
                    if buyMaxMonth[data[2]]==month:
                        monthRight=1
                    else:
                        monthRight=0
                month = str(monthRight)+"M"
                monthLen = -1
                if buyMonthLen.has_key(data[2]):
                    monthLen = buyMonthLen[data[2]]
                file_buys_out.write(str(clickNumber)+","+str(popularOrNot)+","+str(repeat)+","+str(priceGrade)+",'"+categoryValue+"',"+str(maxBuysFrequentness)+
                                    ","+month+","+str(monthLen)+",yes"+"\n")
                beginTime = data[1]
                sessionId = data[0]
                clickInfo= {}
                categoryInfo={}
            clickNumber = 0
            popularOrNot = 0
        else:
            endTime = data[1]
            if popularItem.has_key(data[2]):
                popularOrNot = 1
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]] += 1
        else:
            clickInfo[data[2]] = 1
        clickNumber +=1
        categoryId = data[3].strip()+"C"
        if len(categoryId)>4:
            categoryId = "-1C"
        if categoryId != "0C":
            if categoryInfo.has_key(categoryId):
                categoryInfo[categoryId] += 1
            else:
                categoryInfo[categoryId] = 1
        elif category.has_key(data[2]):
            if categoryInfo.has_key(category[data[2]]):
                categoryInfo[category[data[2]]] += 1
            else:
                categoryInfo[category[data[2]]] = 1
    file_buys_out.close()

def getClickNotBuysFeature(fileOut,buyThreshold):
    file_buys = open('D:\Data\yoochoose-clicks-notBuyData.dat')
    file_buys_out = open(fileOut,"w")
    file_buys_out.write("clickNumber,popularOrNot,repeatClick,priceGrade,categoryValue,buysFrequentness,category\n")
    itemPrice,minPrice,maxPrice = getItemPrice()
    buysFrequentness = getBuysFrequentness('D:\Data\yoochoose-buys-analyse-sorted.dat')
    popularItem = getPopularItem()
    buyMaxMonth = getDicFromFile('D:\Data\yoochoose-buyMaxMonth.dat')
    buyMonthLen = getDicFromFile('D:\Data\yoochoose-buyMonthLen.dat')
    clickInfo={}
    categoryInfo={}
    category = {}
    file_category = open('D:\Data\yoochoose-category.dat')
    for line in file_category:
        category = eval(line)
        break
    beginTime = "-1"
    endTime = "-1"
    sessionId = "-1"
    clickNumber = 0
    popularOrNot = 0
    number = 0
    print "stage 1"
    for line in file_buys:
        if(number%100000==0):
            print number
        number+=1
        data = line.split(",")
        if sessionId != data[0]:
            if sessionId == "-1":
                beginTime = data[1]
                endTime = data[1]
                sessionId = data[0]
            else:
                if clickNumber==1:
                    time = 0
                else :
                    time = calculateTime(beginTime,endTime)
                weekTime = calculateWeekTime(endTime)
                categoryValue = getCategoryValue(categoryInfo)
                repeat,priceGrade,maxBuysFrequentness = repeatOrNot(clickInfo,itemPrice,minPrice,maxPrice,buysFrequentness)
                month = data[1].split("-")[1]
                monthRight = -1
                if buyMaxMonth.has_key(data[2]):
                    if buyMaxMonth[data[2]]==month:
                        monthRight=1
                    else:
                        monthRight=0
                month = str(monthRight)+"M"
                monthLen = -1
                if buyMonthLen.has_key(data[2]):
                    monthLen = buyMonthLen[data[2]]
                file_buys_out.write(str(clickNumber)+","+str(popularOrNot)+","+str(repeat)+","+str(priceGrade)+",'"+categoryValue+"',"+str(maxBuysFrequentness)+
                                    ","+month+","+str(monthLen)+",no"+"\n")
                beginTime = data[1]
                sessionId = data[0]
                clickInfo={}
                categoryInfo={}
            clickNumber = 0
            popularOrNot = 0
        else:
            endTime = data[1]
            if popularItem.has_key(data[2]):
                popularOrNot = 1
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]] += 1
        else:
            clickInfo[data[2]] = 1
        categoryId = data[3].strip()+"C"
        if len(categoryId)>4:
            categoryId = "-1C"
        if categoryId != "0C":
            if categoryInfo.has_key(categoryId):
                categoryInfo[categoryId] += 1
            else:
                categoryInfo[categoryId] = 1
        elif category.has_key(data[2]):
            if categoryInfo.has_key(category[data[2]]):
                categoryInfo[category[data[2]]] += 1
            else:
                categoryInfo[category[data[2]]] = 1
        clickNumber +=1
    file_buys_out.close()
#获得平衡数据集
def getBalanceData(fileNmae,buyFile,clickFile):
    for i in range(17):
        fileName = fileNmae+str(i)+'.arff'
        file_write = open(fileName,'w')
        file_write.write("@relation yoochoose-balance-feature\n\n")
        file_write.write("@attribute clickNumber numeric\n")
        file_write.write("@attribute popularOrNot numeric\n")
        file_write.write("@attribute repeatClick numeric\n")
        file_write.write("@attribute priceGrade numeric\n")
        file_write.write("@attribute categoryValue {3C,1C,0C,9C,7C,2C,4C,5C,6C,SC,8C,-1C,10C,12C,11C,13C,14C,15C,16C,17C,18C,19C,20C,21C,22C,23C,24C,25C,26C,27C,28C,29C,30C}\n")
        file_write.write("@attribute buysFrequentness numeric\n")
        file_write.write("@attribute month {-1M,0M,1M}\n")
        file_write.write("@attribute monthLen numeric\n")
        file_write.write("@attribute category {yes,no}\n\n@data\n")
        file_buys = open(buyFile)
        number=0
        for line in file_buys:
            if number==0:
                number+=1
                continue
            file_write.write(line)
        file_clicks = open(clickFile)
        number=0
        for line in file_clicks:
            if number==0:
                number+=1
                continue
            if (number+i)%17==0:
                file_write.write(line)
            number+=1
        file_write.close()

def getAllData(fileNmae,buyFile,clickFile):
    for i in range(1):
        fileName = fileNmae+str(i)+'.arff'
        file_write = open(fileName,'w')
        file_write.write("@relation yoochoose-balance-feature\n\n")
        file_write.write("@attribute clickNumber numeric\n")
        file_write.write("@attribute popularOrNot numeric\n")
        file_write.write("@attribute repeatClick numeric\n")
        file_write.write("@attribute priceGrade numeric\n")
        file_write.write("@attribute categoryValue {3C,1C,0C,9C,7C,2C,4C,5C,6C,SC,8C,-1C,10C,12C,11C,13C,14C,15C,16C,17C,18C,19C,20C,21C,22C,23C,24C,25C,26C,27C,28C,29C,30C}\n")
        file_write.write("@attribute buysFrequentness numeric\n")
        file_write.write("@attribute month {-1M,0M,1M}\n")
        file_write.write("@attribute category {yes,no}\n\n@data\n")
        file_buys = open(buyFile)
        number=0
        for line in file_buys:
            if number==0:
                number+=1
                continue
            file_write.write(line)
        file_clicks = open(clickFile)
        number=0
        for line in file_clicks:
            if number==0:
                number+=1
                continue
            file_write.write(line)
            number+=1
        file_write.close()
def getTestFeature(fileOut,buyThreshold):
    file_test = open('D:\Data\yoochoose-test.dat')
    file_test_out = open(fileOut,"w")
    buysFrequentness = getBuysFrequentness('D:\Data\yoochoose-buys-analyse-sorted.dat')
    buyMonthLen = getDicFromFile('D:\Data\yoochoose-buyMonthLen.dat')
    file_test_sessionId = open('D:\Data\\feature\yoochoose-test-sessionId.dat',"w")
    #file_test_out.write("clickNumber,weekTime,popularOrNot,repeatClick,priceGrade\n")
    file_test_out.write("@relation yoochoose-test-feature\n\n")
    file_test_out.write("@attribute clickNumber numeric\n")
    file_test_out.write("@attribute popularOrNot numeric\n")
    file_test_out.write("@attribute repeatClick numeric\n")
    file_test_out.write("@attribute priceGrade numeric\n")
    file_test_out.write("@attribute categoryValue {3C,1C,0C,9C,7C,2C,4C,5C,6C,SC,8C,-1C,10C,12C,11C,13C,14C,15C,16C,17C,18C,19C,20C,21C,22C,23C,24C,25C,26C,27C,28C,29C,30C}\n")
    file_test_out.write("@attribute buysFrequentness numeric\n")
    file_test_out.write("@attribute month {-1M,0M,1M}\n")
    file_test_out.write("@attribute monthLen numeric\n")
    file_test_out.write("@attribute category {yes,no}\n\n@data\n")
        
    
    #file_test_out.write("clickNumber,popularOrNot,repeatClick,priceGrade,categoryValue,category\n")
    file_test_sessionId.write("sessionId\n")
    popularItem = getPopularItem()
    itemPrice,minPrice,maxPrice = getItemPrice()
    category = {}
    file_category = open('D:\Data\yoochoose-category.dat')
    buyMaxMonth = getDicFromFile('D:\Data\yoochoose-buyMaxMonth.dat')
    for line in file_category:
        category = eval(line)
        break
    beginTime = "-1"
    endTime = "-1"
    sessionId = "-1"
    clickInfo = {}
    categoryInfo = {}
    s={}
    clickNumber = 0
    popularOrNot = 0
    for line in file_test:
        data = line.split(",")
        if sessionId != data[0]:
            if sessionId == "-1":
                beginTime = data[1]
                endTime = data[1]
                sessionId = data[0]
            else:
                if clickNumber==1:
                    time = 0
                else :
                    time = calculateTime(beginTime,endTime)
                weekTime = calculateWeekTime(endTime)
                categoryValue = getCategoryValue(categoryInfo)
                repeat,priceGrade,maxBuysFrequentness = repeatOrNot(clickInfo,itemPrice,minPrice,maxPrice,buysFrequentness)
                month = data[1].split("-")[1]
                monthRight = -1
                if buyMaxMonth.has_key(data[2]):
                    if buyMaxMonth[data[2]]==month:
                        monthRight=1
                    else:
                        monthRight=0
                month = str(monthRight)+"M"
                monthLen = -1
                if buyMonthLen.has_key(data[2]):
                    monthLen = buyMonthLen[data[2]]
                file_test_out.write(str(clickNumber)+","+str(popularOrNot)+","+str(repeat)+","+str(priceGrade)+",'"+categoryValue+"',"+str(maxBuysFrequentness)+
                                    ","+month+","+str(monthLen)+",?"+"\n")

                file_test_sessionId.write(str(sessionId)+"\n")
                beginTime = data[1]
            sessionId = data[0]
            clickNumber = 0
            popularOrNot = 0
            clickInfo={}
            categoryInfo ={}
            s={}
        else:
            endTime = data[1]
            if popularItem.has_key(data[2]):
                popularOrNot = 1
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]] += 1
        else:
            clickInfo[data[2]] = 1
        categoryId = data[3].strip()+"C"
        if len(categoryId)>4:
            categoryId = "-1C"
        if categoryId != "0C":
            if categoryInfo.has_key(categoryId):
                categoryInfo[categoryId] += 1
            else:
                categoryInfo[categoryId] = 1
        elif category.has_key(data[2]):
            if categoryInfo.has_key(category[data[2]]):
                categoryInfo[category[data[2]]] += 1
            else:
                categoryInfo[category[data[2]]] = 1
        clickNumber +=1
        s[data[2]] = 1
    file_test_out.close()
  
#generateCategoryValue()
#getBuysFeature('D:\Data\\feature\yoochoose-buys-click-feature-maxBuysFrequentness-monthLen.csv',10)#获得购买点击的特征

#getClickNotBuysFeature('D:\Data\\feature\yoochoose-notBuys-click-feature-maxBuysFrequentness-monthLen.csv',10)
#getTestFeature('D:\Data\\feature\yoochoose-test-feature-maxBuysFrequentness-monthLen.arff',10)
#getBalanceData('D:\Data\\feature\\balance-monthLen\yoochoose-feature-balence-',
 #              'D:\Data\\feature\yoochoose-buys-click-feature-maxBuysFrequentness-monthLen.csv',
  #             'D:\Data\\feature\yoochoose-notBuys-click-feature-maxBuysFrequentness-monthLen.csv')
'''getAllData('D:\Data\\feature\\balance-month\yoochoose-feature-all-',
               'D:\Data\\feature\yoochoose-buys-click-feature-maxBuysFrequentness-monthLen.csv',
               'D:\Data\\feature\yoochoose-notBuys-click-feature-maxBuysFrequentness-monthLen.csv')
'''

