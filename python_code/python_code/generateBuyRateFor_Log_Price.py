# -*- coding: cp936 -*-
import string
import random
import math
#获得商品价格
def getItemPrice():
    file_buys = open('D:\Data\yoochoose-buys.dat')
    maxPrice = 0
    minPrice = 100000
    itemPrice = {}
    for line in file_buys:
        data = line.split(",")
        itemId = data[2]  #itemId
        price = string.atoi(data[3])
        itemPrice[itemId] = price
        if price>maxPrice:
            maxPrice = price
        if price<minPrice:
            minPrice = price
    return itemPrice,minPrice,maxPrice

def getPriceGrade(price,minPrice,maxPrice):
    return int(math.log10(price+1))
    #gradeInteval = (maxPrice-minPrice)/5+1
    #return (price-minPrice)/gradeInteval

def getBuyNumberForGrade(itemPrice,minPrice,maxPrice,grade):  
    buyNumberForGrade  = {}  #购买的项目的价格的等级及其出现的次数
    file_buys = open('D:\Data\yoochoose-buys.dat')
    for line in file_buys:
        data =line.split(",")
        itemId = data[2]
        if itemPrice.has_key(itemId):
            priceGrade = getPriceGrade(itemPrice[itemId],minPrice,maxPrice)
            if buyNumberForGrade.has_key(priceGrade):
                buyNumberForGrade[priceGrade]+=1
            else: buyNumberForGrade[priceGrade]=1
    return buyNumberForGrade
def getClickNumberForGrade(itemPrice,minPrice,maxPrice,grade):    
    clickNumberForGrade  = {} #点击的项目价格的等级及其出现的次数
    file_buys = open('D:\Data\yoochoose-clicks.dat')
    for line in file_buys:
        data =line.split(",")
        itemId = data[2]
        if itemPrice.has_key(itemId):
            priceGrade = getPriceGrade(itemPrice[itemId],minPrice,maxPrice)
            if clickNumberForGrade.has_key(priceGrade):
                clickNumberForGrade[priceGrade]+=1
            else: clickNumberForGrade[priceGrade]=1
    return clickNumberForGrade

def generateBuyRateFor_Log_Price():
    itemPrice,minPrice,maxPrice = getItemPrice()
    grade = 6
    buyNumberForGrade = getBuyNumberForGrade(itemPrice,minPrice,maxPrice,grade)
    clickNumbeForGrade = getClickNumberForGrade(itemPrice,minPrice,maxPrice,grade)
    for index in buyNumberForGrade:
        if clickNumbeForGrade.has_key(index):
            print index,'\t',buyNumberForGrade[index],'\t',clickNumbeForGrade[index],'\t',1.0*buyNumberForGrade[index]/clickNumbeForGrade[index]
