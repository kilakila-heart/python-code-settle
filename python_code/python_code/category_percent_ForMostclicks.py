# --*coding:cp936 --*
import math
import string 
#生成购买点击最多的商品占总购买的比例
def category_percent_ForMostclicks():
   
    file_buys = open('D:\Data\yoochoose-buys-sorted.dat')
    file_clicks_buysOnly = open('D:\Data\yoochoose-clicks-hasBuyData-sorted')
    sessionId = "-1"
    mostClick = {}#能记录hasbuydata中的会话即这次会话中受到最大点击的项目的类别
    clickInfo = {} #这里的clickInfo能记录hasbuy中出现的项目的类别及其次数
    for line in file_clicks_buysOnly:
        data = line.split(",") #data形如[11,2014-04-03T11:04:11.417Z,214821371,1046,1]
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                clickInfo = sorted(clickInfo.iteritems(),key=lambda s:s[1],reverse=True)
                for clickInfo_ in clickInfo:
                    mostClick[sessionId] = clickInfo_[0]   #mostClick形如：{sessionId:受到最大点击的caterory}
		    
                    #且已经按照了项目的类别点击次数对项目出现的位置进行了排序
                    #即mostclick中存放的是会话和此会话中1被操作最多的项目
                    break
                clickInfo = {}
        sessionId = data[0]
        if clickInfo.has_key(data[3].strip()):
            clickInfo[data[3].strip()]+=1 #clickInfo形如:{itemId1:次数,itemId2:次数..}}
        else:
            clickInfo[data[3].strip()] = 1
    number = 0
    totalNumber = 0
    sessionId = "-1"
    itemCategory=getItemcategory()
    itemPrice=getDicFromFile('D:\Data\yoochoose-buys-itemPrice.dat')
    for line in file_buys:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                if itemCategory[data[2]]==mostClick[sessionId]:#
                    number +=1    #蕴含着对最流行类别点击的购买的buy中的相应的Session
                totalNumber += 1     ###totalNumber表示buy中总的Session数        
        sessionId= data[0]
    
    print number                   #100271           
    print totalNumber              #509695
    print 1.0*number/totalNumber   #0.196727454654
#获得Item及category的字典
def getItemcategory():
    file_clicks=open('D:\Data\yoochoose-clicks.dat')
    itemCategory={}
    i=0
    number=0
    for line in file_clicks:
        number+=1
        if number%100000==0:
            print number
        data = line.split(",")
        itemId = data[2]
        Category =data[3].strip()
        if itemCategory.has_key(itemId):
            i+=1                      #
        itemCategory[itemId] = Category
  #      itemCategory[itemId][Category]=i
    print i   #32951205
    return itemCategory
def getDicFromFile(fileName):
    file1 = open(fileName)
    dic = {}
    for line in file1:
        dic = eval(line)
    return dic
category_percent_ForMostclicks()














