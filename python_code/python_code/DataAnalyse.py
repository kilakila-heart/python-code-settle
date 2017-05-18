# -*- coding: cp936 -*-
import string
import random
import math
def sortBuysViaSessionId(inFile,outFile):       #把buys里的数据根据sessionID排序
#sortBuysViaSessionId('D:\Data\yoochoose-buys.dat','D:\Data\yoochoose-buys-sorted.dat')
    file_object = open(inFile) 
    file_object_w = open(outFile, 'w')

    s = {}
    number = 0
    for line in file_object:   #11,2014-04-03T11:04:11.417Z,214821371,1046,1
        if number%100000 ==0:
            print number
        number+=1    
        index = line.split(",")[0]
        s[line] = string.atoi(index)
    s = sorted(s.iteritems(),key=lambda s:s[1],reverse=False)
    for line in s:
        file_object_w.write(line[0])
    file_object_w.close()


def calculateItemOperation(inFile,outFile):          #统计item被操作（购买/点击）的次数，并排序输出
#calculateItemOperation('D:\Data\yoochoose-clicks.dat','D:\Data\yoochoose-clicks-analyse-sorted.dat')
#calculateItemOperation('D:\Data\yoochoose-buys.dat','D:\Data\yoochoose-buys-analyse-sorted.dat')
    file_object = open(inFile)
    file_object_w = open(outFile, 'w')

    s = {}
    number = 0
    for line in file_object:
        if number%100000 ==0:
            print number
        number+=1    
        index = line.split(",")[2]
        if s.has_key(index):
            s[index]+= 1
        else:
            s[index] = 1
    s = sorted(s.iteritems(),key=lambda s:s[1],reverse=True)
    for line in s:
        file_object_w.write(line[0]+ "\t" + str(line[1])+"\n")

    file_object_w.close()

def calculateItem_Log(inFile,outFile):          #统计item被操作（购买/点击）的次数，以log形式表示并排序输出
#calculateItemOperation('D:\Data\yoochoose-clicks.dat','D:\Data\yoochoose-clicks-analyse-Log_sorted.dat')
#calculateItemOperation('D:\Data\yoochoose-buys.dat','D:\Data\yoochoose-buys-analyse-Log_sorted.dat')
    file_object = open(inFile)
    file_object_w = open(outFile, 'w')

    s = {}
    number = 0
    for line in file_object:
        if number%100000 ==0:
            print number
        number+=1    
        index = line.split(",")[2]
        if s.has_key(index):
            s[index]+= 1
        else:
            s[index] = 1
    s = sorted(s.iteritems(),key=lambda s:s[1],reverse=True)
    for line in s:
        file_object_w.write(str(math.log10(string.atoi(line[0])))+ "\t" + str(math.log10(line[1]))+"\n")

    file_object_w.close()
####以下代码图形那里还要注意下
def generateBuysVsClicks(inFile1,inFile2,outFile):                      #生成商品总的购买点击比并排序，同时保留购买数与点击数
#generateBuysVsClicks('D:\Data\yoochoose-buys-analyse-sorted.dat',
#'D:\Data\yoochoose-clicks-analyse-sorted.dat','D:\Data\\buy_vs_clicks.txt')
    file_object1 = open(inFile1)
    file_object2 = open(inFile2)
    file_object_w = open(outFile,'w')
    s1={}
    s2={}
    for line in file_object1:
        s1[line.split("\t")[0]]=str(string.atoi(line.split("\t")[1]))
    for line in file_object2:
        inf = line.split("\t")
        if s1.has_key(inf[0]):
            s2[inf[0]+"\t"+s1[inf[0]]+"\t"+str(string.atoi(inf[1]))] =  "%.2f" % (string.atof(s1[inf[0]]) /string.atof(inf[1]))
    s2 = sorted(s2.iteritems(),key=lambda s:s[1],reverse=True)
    file_object_w.write("sessionId\tbuy\tclick\tbuy/click\n")
    for s_ in s2:
        file_object_w.write(str(s_[0])+"\t"+s_[1]+"\n")
    file_object_w.close()

def generateClicksHasBuys(inFileBuys,inFileClicks,outFile,outFile2):
##generateClicksHasBuys("D:\Data\yoochoose-buys.dat","D:\Data\yoochoose-clicks.dat",
#"D:\Data\yoochoose-clicks-hasBuyData.dat", "D:\Data\yoochoose-clicks-notBuyData.dat")
    file_objectB = open(inFileBuys)
    file_objectC = open(inFileClicks)
    file_object_w = open(outFile, 'w')
    file_object_w2 = open(outFile2, 'w')
    s = {}
    numberAll = 0
    number = 0 
    for line in file_objectB:
        s[line.split(",")[0]]=1
    for line in file_objectC:
        numberAll+=1
        itemId = line.split(",")[0]
        if s.has_key(itemId):
            number+=1
            file_object_w.write(line)
        else:
            file_object_w2.write(line)
    file_object_w.close()
    file_object_w2.close()
    print number #3305687   #hasBuyData中总的行数
    print numberAll #33003944次点击,表示click中总的行数，即点击数
    
#生成购买点击最多的商品占总购买的比例
def percentForMostclicks():
    file_buys = open('D:\Data\yoochoose-buys-sorted.dat')
    file_clicks_buysOnly = open('D:\Data\yoochoose-clicks-hasBuyData-sorted')
    sessionId = "-1"
    mostClick = {}   #能记录hasbuydata中的会话即这次会话中受到最大点击的ItemID
    clickInfo = {} #这里的clickInfo能记录hasbuy中出现的项目及其次数
    for line in file_clicks_buysOnly:
        data = line.split(",") #data形如[11,2014-04-03T11:04:11.417Z,214821371,1046,1]
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                clickInfo = sorted(clickInfo.iteritems(),key=lambda s:s[1],reverse=True)
                for clickInfo_ in clickInfo:
                    mostClick[sessionId] = clickInfo_[0]   #mostClick形如：{sessionId:受到最大点击的itemId}
		    
                    #且已经按照了项目的点击次数对项目出现的位置进行了排序
                    #即mostclick中存放的是会话和此会话中1被操作最多的项目
                    break
                clickInfo = {}
        sessionId = data[0]
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]]+=1 #clickInfo形如:{itemId1:次数,itemId2:次数..}}
        else:
            clickInfo[data[2]] = 1
    number = 0
    totalNumber = 0
    sessionId = "-1"
    buysInfo = {}
    for line in file_buys:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                if buysInfo.has_key(mostClick[sessionId]):#
                    number +=1    #蕴含着对最流行商品点击的Session中的itemID的购买的buy中的相应的Session
                totalNumber += 1     ###totalNumber表示buy中总的Session数        
                buysInfo = {}
        buysInfo[data[2]] = 1
        sessionId= data[0]
    
    print number                   #401179               
    print totalNumber              #509695 buy中总的项目数
    print 1.0*number/totalNumber   #0.787096204593  
#生成每一百个商品点击的购买率分布
def generateBuysRate():###############@@@@@@@@@################################？？
    file_buys = open('D:\Data\yoochoose-clicks-buys-feature.dat')
    buysNumber = {}
    inteval  = 1000
    for line in file_buys:
        session = string.atoi(line.split("\t")[0])/inteval
        if buysNumber.has_key(session):
            buysNumber[session]+=1
        else:
            buysNumber[session] = 1
    file_clicks = open('D:\Data\yoochoose-clicks-feature.csv')
    clickNumbers = {}
    for line in file_clicks:
        session = string.atoi(line.split(",")[0])/inteval
        if clickNumbers.has_key(session):
            clickNumbers[session]+=1
        else:
            clickNumbers[session] = 1
    a = [0 for i in range(101)]
    buyNumber = 0
    totalNumber = 0
    for clickId in clickNumbers:
        if buysNumber.has_key(clickId):
            rate = buysNumber[clickId]*100/clickNumbers[clickId]
            buyNumber += buysNumber[clickId]
        else:
            rate = 0
        if rate>100:
            print clickId, buysNumber[clickId],clickNumbers[clickId]
        a[rate]+=1
        totalNumber +=clickNumbers[clickId]
    for i in range(101):
        print str(i)+"\t"+str(a[i])
    print 1.0*buyNumber/totalNumber
#获得商品价格
def getItemPrice():
    file_buys = open('D:\Data\yoochoose-buys.dat')
    file_item_price=open('D:\\Data\\yoochoose-buys-itemPrice.dat','w')
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
    file_item_price.write(str(itemPrice))
    return itemPrice,minPrice,maxPrice
def getBuyNumberForGrade(itemPrice,minPrice,maxPrice,grade):
    dividedNumber = (maxPrice-minPrice)/grade+1 #分割的区间
    buyNumberForGrade  = {}  #购买的项目的价格的等级及其出现的次数
    file_buys = open('D:\Data\yoochoose-buys.dat')
    for line in file_buys:
        data =line.split(",")
        itemId = data[2]
        if itemPrice.has_key(itemId):
            priceGrade = (itemPrice[itemId]-minPrice)/dividedNumber
            if buyNumberForGrade.has_key(priceGrade):
                buyNumberForGrade[priceGrade]+=1
            else: buyNumberForGrade[priceGrade]=1
    return buyNumberForGrade
def getClickNumberForGrade(itemPrice,minPrice,maxPrice,grade):
    dividedNumber = (maxPrice-minPrice)/grade+1
    clickNumberForGrade  = {} #点击的项目价格的等级及其出现的次数
    file_buys = open('D:\Data\yoochoose-clicks.dat')
    for line in file_buys:
        data =line.split(",")
        itemId = data[2]
        if itemPrice.has_key(itemId):
            priceGrade = (itemPrice[itemId]-minPrice)/dividedNumber
            if clickNumberForGrade.has_key(priceGrade):
                clickNumberForGrade[priceGrade]+=1
            else: clickNumberForGrade[priceGrade]=1
    return clickNumberForGrade
#获得不同价格梯度的点击购买比   ####始终不明白这里的用处在哪里？
def generateBuyRateForPrice():
    itemPrice,minPrice,maxPrice = getItemPrice()
    grade = 5
    buyNumberForGrade = getBuyNumberForGrade(itemPrice,minPrice,maxPrice,grade)
    clickNumbeForGrade = getClickNumberForGrade(itemPrice,minPrice,maxPrice,grade)
    for index in buyNumberForGrade:
        if clickNumbeForGrade.has_key(index):
            print index,1.0*buyNumberForGrade[index]/clickNumbeForGrade[index]
def generateBuyRateForRepeatClick():
    file_clicks_buys = open('D:\Data\yoochoose-clicks-hasBuyData-sorted')
    file_clicks_notBuys = open('D:\Data\yoochoose-clicks-notBuyData.dat')
    sessionId = "-1"
    repeatBuysClickNumber = {}
    clickInfo = {} #统计clicks-hasBuyData出现的项目及其出现的次数
    for line in file_clicks_buys:
        data = line.split(",") #[11,2014-04-03T10:57:19.331Z,214826837,0]
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                repeatNumber = 0
                for clickInfo_ in clickInfo:     #按键遍历
                    if clickInfo[clickInfo_]>1:  #clickInfo形如:{项目1:被点击的次数,项目2:被点击的次数,..}
                        repeatNumber+=1           #repeatNumber表示一次会话中项目有多少个项目被多次点击则加多少个1！
                if repeatBuysClickNumber.has_key(repeatNumber):
                    repeatBuysClickNumber[repeatNumber]+=1
                else:                                     #重复点击的次数从一开始计数
                    repeatBuysClickNumber[repeatNumber]=1 #repeatBuysClickNumber形如{重复点击的次数:重复点击的次数出现的次数...}
                clickInfo = {}
        sessionId = data[0]
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]]+=1
        else:
            clickInfo[data[2]] = 1
            
    sessionId = "-1"
    repeatNotBuysClickNumber = {}
    clickInfo = {}
    for line in file_clicks_notBuys:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                repeatNumber = 0
                for clickInfo_ in clickInfo:
                    if clickInfo[clickInfo_]>1:
                        repeatNumber+=1
                if repeatNotBuysClickNumber.has_key(repeatNumber):
                    repeatNotBuysClickNumber[repeatNumber]+=1
                else:
                    repeatNotBuysClickNumber[repeatNumber]=1
                clickInfo = {}
        sessionId = data[0]
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]]+=1
        else:
            clickInfo[data[2]] = 1
    repeatBuysClickNumber = sorted(repeatBuysClickNumber.iteritems(),key=lambda s:s[0],reverse=False)
    for number_ in repeatBuysClickNumber:    ####按键值对遍历
        if repeatNotBuysClickNumber.has_key(number_[0]):
#print(repeatBuysClickNumber中记录的重复点击的次数,repeatBuysClickNumber重复点击的次数出现的次数)\t
#repeatBuysClickNumber中记录的重复点击的次数/(repeatNotBuysClickNumber[number_[0]]+number_[1])
            print str(number_)+"\t"+str(1.0*number_[1]/(repeatNotBuysClickNumber[number_[0]]+number_[1]))
            
#生成小于10000的click数据
def generateSmallClickData(number):
    file_clicks_clicks = open('D:\Data\yoochoose-clicks.dat')
    file_clicks_out = open('D:\Data\yoochoose-clicks-small.dat','w')
    for line in file_clicks_clicks:
        data = line.split(",")
        if string.atoi(data[0])>number:
            break
        file_clicks_out.write(line)
    file_clicks_out.close()
#统计包含各种种类的购买点击比
def generateCategoryBuysRate():   
    file_buys = open('D:\Data\yoochoose-buys.dat')
    session_buy = {} #包含buy中所有SessionID的字典
    for line in file_buys:
        session_buy[line.split(",")[0]] = 1 #session_buy形如:{sessionId1:1,session2:1....}
    
    category = {}
    file_category = open('D:\Data\yoochoose-category.dat')
    for line in file_category:
        category = eval(line)   #category能得到所有buy中的项目及项目类别的字典
        break
    
    tmp = 0
    print len(category)  #52739   此即得到的click中出现的所有ItemID的总数
    file_click = open('D:\Data\yoochoose-clicks.dat')
    sessionId = "-1"
    clickInfo = {}
    category_buyNumber = {}
    category_notBuyNumber = {}
    for line in file_click:
        data = line.split(",") #data形如[1,2014-04-07T10:51:09.277Z,214536502,0]
        data[3] = data[3].strip() #data[3]即项目的category
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                repeatNumber = 0
                if session_buy.has_key(sessionId):#如果click中的此Session也在buy中出现
                    for clickInfo_ in clickInfo:
                        if category_buyNumber.has_key(clickInfo_):
                            category_buyNumber[clickInfo_]+=1  #buy和click中相同会话相同类别计数
                        else:
                            category_buyNumber[clickInfo_]=1
                else:
                    for clickInfo_ in clickInfo:
                        if category_notBuyNumber.has_key(clickInfo_):
                            category_notBuyNumber[clickInfo_]+=1
                        else:
                            category_notBuyNumber[clickInfo_]=1#相同会话中出现在click中的category而没出现在buy中的category计数
                clickInfo = {}
        sessionId = data[0]
        if data[3] != "0":            #data[3]表示category
            clickInfo[data[3]] = 1
        elif category.has_key(data[2]):         #data[2]表示itemID
            clickInfo[category[data[2]]] = 1    #最终categoryinfo会拿出category中所有的类别
    for categoryId in category_buyNumber:
        if category_notBuyNumber.has_key(categoryId):
            print categoryId+"\t"+str(category_buyNumber[categoryId])+"\t"+str(category_notBuyNumber[categoryId])+"\t"+str(1.0*category_buyNumber[categoryId]/(category_buyNumber[categoryId]+category_notBuyNumber[categoryId]))


def generateBuysSession(buysFile,outputFile):#得到buy文件中所有的SessionID
    buysInfo = {}
    file_buys = open(buysFile)
    for session in file_buys:
        data = session.split(",")
        buysInfo[data[0]] = 1
    file_buys_info = open(outputFile,'w')
    file_buys_info.write(str(buysInfo))
    file_buys_info.close()
def getBuysInfo(buysInfoFile):
    file_buys_info = open(buysInfoFile)
    buysInfo = {}
    for line in file_buys_info:
        buysInfo = eval(line)
        break
    return buysInfo

def dicAdd(dic,key):
    if dic.has_key(key):
        dic[key]+=1
    else:
        dic[key] = 1

def generateOneClickBuysRate(buyInfoFile,clicksFile,oneClickBuysRateFileOut):
    buysInfo = getBuysInfo(buyInfoFile)
    file_clicks = open(clicksFile)
    file_out = open(oneClickBuysRateFileOut,'w')
    itemInfoBuys = {}
    itemInfoAll = {}
    sessionId = "-1"
    itemId = "-1"
    eachNumber = 0
    for line in file_clicks:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId != "-1":
                if eachNumber==1:
                    if buysInfo.has_key(sessionId):
                        dicAdd(itemInfoBuys,itemId)
                    dicAdd(itemInfoAll,itemId)
            eachNumber = 0
        sessionId = data[0]
        itemId = data[2]
        eachNumber+=1
    oneClickBuysRate = {}
    for itemId in itemInfoBuys:
        oneClickBuysRate[itemId] = 1.0*itemInfoBuys[itemId]/itemInfoAll[itemId]   
    file_out.write(str(oneClickBuysRate))
    file_out.close()
def analyseOneClickData():
    #
    buysInfo = getBuysInfo('D:\Data\yoochoose-buys-info.dat')
    file_clicks = open('D:\Data\yoochoose-clicks.dat')
    sessionId = "-1"
    totalSession = 0
    eachNumber = 0
    oneClickBuySession=0
    oneClickSession=0
    buysClickNumber = {}
    totalClickNumber = {}
    for line in file_clicks:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId != "-1":
                totalSession+=1
                if buysInfo.has_key(sessionId):
                    dicAdd(buysClickNumber,eachNumber)
                dicAdd(totalClickNumber,eachNumber) 
            eachNumber = 0
        sessionId = data[0]
        eachNumber+=1
    buyRate = {}
    print "buysClickNumber:\n"
    for index in buysClickNumber:
        print str(index)+"\t"+str(buysClickNumber[index])
    print "totalClickNumber:\n"
    for index in totalClickNumber:
        if buysClickNumber.has_key(index):
            buyRate[index] = 1.0*buysClickNumber[index]/totalClickNumber[index]
        print str(index)+"\t"+str(totalClickNumber[index])
    print "buyRate:\n"
    for index in buyRate:
        print str(index)+"\t"+str(buyRate[index])
    #totalBuySession = len(buysInfo)
    #print [totalSession,totalBuySession] #[9249728, 509696]
    #print [oneClickSession,oneClickBuySession] #[1259711, 22363]
def analyseResultData(resultFile):
    #click数量分布
    buysResult = {}
    buysClickNumber = {}
    file_result = open(resultFile)
    for line in file_result:
        data = line.split(";")
        buysResult[data[0]] = 1
    file_test = open('D:\Data\yoochoose-test.dat')
    sessionId = "-1"
    eachNumber = 0
    for line in file_test:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId != "-1":
                if buysResult.has_key(sessionId):
                    dicAdd(buysClickNumber,eachNumber)
            eachNumber = 0
        sessionId = data[0]
        eachNumber+=1
    for index in buysClickNumber:
        print str(index)+"\t"+str(buysClickNumber[index])

def doubleClickBuyRate():
    buysInfo = getBuysInfo('D:\Data\yoochoose-buys-info.dat')
    sessionId = "-1"
    file_clicks = open('D:\Data\yoochoose-clicks.dat')
    doubleClickAndBuy= 0
    noDoubleClickAndBuy = 0
    totalDoubleClick = 0
    totalNoDoubleClick = 0
    noDoubleClickLengthDis = {}
    totalNoDoubleClickLengthDis = {}
    clickInfo = {}
    for line in file_clicks:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId != "-1":
                dc = 0
                for info in clickInfo:
                    if clickInfo[info]>1:
                        dc = 1
                clickLength = len(clickInfo)
                if dc==1:
                    if buysInfo.has_key(sessionId):
                        doubleClickAndBuy+=1
                    totalDoubleClick+=1
                else:
                    if buysInfo.has_key(sessionId):
                        noDoubleClickAndBuy+=1
                        dicAdd(noDoubleClickLengthDis,clickLength)
                    totalNoDoubleClick+=1
                    dicAdd(totalNoDoubleClickLengthDis,clickLength)
                clickInfo = {}
        sessionId = data[0]
        dicAdd(clickInfo,data[2])
    #print [doubleClickAndBuy,totalDoubleClick,1.0*doubleClickAndBuy/totalDoubleClick]#[347569, 3369614, 0.10314801636033089]
    #print [noDoubleClickAndBuy,totalNoDoubleClick,1.0*noDoubleClickAndBuy/totalNoDoubleClick] #[162127, 588011  , 0.027572084486797366]
    for length in noDoubleClickLengthDis:
        print str(length)+"\t"+str(1.0*noDoubleClickLengthDis[length]/totalNoDoubleClickLengthDis[length])
    #for length in totalNoDoubleClickLengthDis:
    #   print str(length)+"\t"+str(1.0*totalNoDoubleClickLengthDis[length]/noDoubleClickLengthDis[length])
def itemMonthDis(itemId):
    file_clicks = open('D:\Data\yoochoose-clicks.dat')
    file_buys = open('D:\Data\yoochoose-buys.dat')
    buyMonthDis = {}
    clickMonthDis = {}
    for line in file_buys:
        data = line.split(",")
        itemIdNow = data[2]
        if itemIdNow == itemId:
            dicAdd(buyMonthDis,(data[1].split("-"))[1])
    for month in buyMonthDis:
        print month+"\t"+str(buyMonthDis[month])
    
    for line in file_clicks:
        data = line.split(",")
        itemIdNow = data[2]
        if itemIdNow == itemId:
            dicAdd(clickMonthDis,(data[1].split("-"))[1])
    for month in clickMonthDis:
        print month+"\t"+str(1.0*buyMonthDis[month]/clickMonthDis[month])
#itemMonthDis('214850947')
def generateItemMonth():
    file_buys = open('D:\Data\yoochoose-buys.dat')
    file_buyMaxMonth = open('D:\Data\yoochoose-buyMaxMonth.dat','w')
    file_buyMonthLen = open('D:\Data\yoochoose-buyMonthLen.dat','w')
    buyMonthDis={}
    for line in file_buys:
        data = line.split(",")
        month = (data[1].split("-"))[1]
        itemIdNow = data[2]
        if not buyMonthDis.has_key(itemIdNow):
            buyMonthDis[itemIdNow]={}
        if buyMonthDis[itemIdNow].has_key(month):
            buyMonthDis[itemIdNow][month]+=1
        else:
            buyMonthDis[itemIdNow][month]=1
    buyMaxMonthDis = {}
    buyMonthLen = {}
    for itemId in buyMonthDis:
        maxMonth = "-1"
        maxNumber = 0
        for month in buyMonthDis[itemId]:
            if buyMonthDis[itemId][month]>maxNumber:
                maxNumber = buyMonthDis[itemId][month]
                maxMonth = month
        buyMaxMonthDis[itemId] = month
        buyMonthLen[itemId] = len(buyMonthDis[itemId])
    file_buyMaxMonth.write(str(buyMaxMonthDis))
    file_buyMonthLen.write(str(buyMonthLen))
    file_buyMaxMonth.close()
    file_buyMonthLen.close()
def buyRateContextAware():
    buyClickRate = {}
    buyNumber = {}
    clickNumber = {}

def analyseNClick(N):
    buysInfo = getBuysInfo('D:\Data\yoochoose-buys-info.dat')
    file_clicks = open('D:\Data\yoochoose-clicks.dat')
    sessionId = "-1"
    orderClick = {}
    buySessionOrderClick = {}
    buySessionOrderClickTmp = {}
    orderClickBuyRate = {}
    click = {}
    choosed = {}
    number = 0
    repeated = 0
    newNumber = 0
    orderClickTmp = {}
    for line in file_clicks:
        data = line.split(",")
        if sessionId != data[0]:
            if sessionId != "-1":
                if repeated==0 and len(click)==N:
                    for click in orderClickTmp:
                        if orderClick.has_key(click):
                            orderClick[click]+=orderClickTmp[click]
                        else:
                            orderClick[click]=orderClickTmp[click]
                    for click in buySessionOrderClickTmp:
                        if buySessionOrderClick.has_key(click):
                            buySessionOrderClick[click]+=buySessionOrderClickTmp[click]
                        else:
                            buySessionOrderClick[click]=buySessionOrderClickTmp[click]
                number = 0
                click = {}
                choosed = {}
                orderClickTmp = {}
                buySessionOrderClickTmp = {}
                repeated = 0
        sessionId = data[0]
        if not choosed.has_key(data[2]):
            click[number] = data[2]
            number = (number+1)%N
        if choosed.has_key(data[2]):
            repeated = 1
        choosed[data[2]] = 1
        if len(click)==N:
            s = ""
            for i in range(N):
                s +=("_" + click[(number+1+i)%N])
            if orderClickTmp.has_key(s):
                orderClickTmp[s]+=1
            else:
                orderClickTmp[s]=1
            if buysInfo.has_key(sessionId):
                if buySessionOrderClickTmp.has_key(s):
                    buySessionOrderClickTmp[s]+=1
                else:
                    buySessionOrderClickTmp[s]=1
    for click in  buySessionOrderClick:
        if buySessionOrderClick[click]>10:
            orderClickBuyRate[click] = 1.0*buySessionOrderClick[click]/orderClick[click]
    orderClickBuyRate = sorted(orderClickBuyRate.iteritems(),key=lambda s:s[1],reverse=True)
    print "orderClickBuyRate"
    for i in range(10):
        print orderClickBuyRate[i][0]+"\t"+str(orderClickBuyRate[i][1])+"\t"+str(buySessionOrderClick[orderClickBuyRate[i][0]])+"\t"+str(orderClick[orderClickBuyRate[i][0]])
    orderClick = sorted(orderClick.iteritems(),key=lambda s:s[1],reverse=True)
    buySessionOrderClick = sorted(buySessionOrderClick.iteritems(),key=lambda s:s[1],reverse=True)
    print "orderClick"
    for i in range(10):
        print orderClick[i][0]+"\t"+str(orderClick[i][1])
    print "buySessionOrderClick"
    for i in range(10):
        print buySessionOrderClick[i][0]+"\t"+str(buySessionOrderClick[i][1])
def getYesterdayBuyNumber(itemId,month,day):
    totalBuyNumber = 0
    yesterdayBuyNumber = 0
#def generateBuyNumber(fileName):
    


    

#generateItemMonth()
#doubleClickBuyRate()
#sortBuysViaSessionId('D:\Data\yoochoose-buys.dat','D:\Data\yoochoose-buys-sorted.dat')      #把buys里的数据根据sessionID排序
#calculateItemOperation('D:\Data\yoochoose-clicks.dat','D:\Data\yoochoose-clicks-analyse-sorted.dat')  #统计item被点击数据的次数，并排序输出
#calculateItemOperation('D:\Data\yoochoose-buys.dat','D:\Data\yoochoose-buys-analyse-sorted.dat')  #统计item被点击购买的次数，并排序输出

#generateBuysVsClicks('D:\Data\yoochoose-buys-analyse-sorted.dat',
#                     'D:\Data\yoochoose-clicks-analyse-sorted.dat','D:\Data\\buy_vs_clicks.txt')    #生成商品总的购买点击比并排序，同时保留购买数与点击数

#generateClicksHasBuys("D:\Data\yoochoose-buys.dat",
#                      "D:\Data\yoochoose-clicks.dat",
#                      "D:\Data\yoochoose-clicks-hasBuyData.dat",
#                      "D:\Data\yoochoose-clicks-notBuyData.dat")
#percentForMostclicks()
#generateBuysRate()
#generateBuyRateForPrice()
#generateBuyRateForRepeatClick()
#generateCategoryBuysRate()
#generateSmallClickData(100000)
#generateOneClickBuysRate('D:\Data\yoochoose-buys-info.dat','D:\Data\yoochoose-clicks.dat','D:\Data\yoochoose-buysRate-oneClick.dat')
#analyseOneClickData()
#analyseResultData("D:\\Data\\solution\\lastsolution-combine\\-and.dat")
#analyseResultData("D:\\Data\\solution\\lastsolution-form\\10-10-0.05")
