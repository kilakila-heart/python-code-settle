# --*coding:cp936 --*
import math
import string 
#���ɹ�����������Ʒռ�ܹ���ı���
def category_percent_ForMostclicks():
   
    file_buys = open('D:\Data\yoochoose-buys-sorted.dat')
    file_clicks_buysOnly = open('D:\Data\yoochoose-clicks-hasBuyData-sorted')
    sessionId = "-1"
    mostClick = {}#�ܼ�¼hasbuydata�еĻỰ����λỰ���ܵ����������Ŀ�����
    clickInfo = {} #�����clickInfo�ܼ�¼hasbuy�г��ֵ���Ŀ����������
    for line in file_clicks_buysOnly:
        data = line.split(",") #data����[11,2014-04-03T11:04:11.417Z,214821371,1046,1]
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                clickInfo = sorted(clickInfo.iteritems(),key=lambda s:s[1],reverse=True)
                for clickInfo_ in clickInfo:
                    mostClick[sessionId] = clickInfo_[0]   #mostClick���磺{sessionId:�ܵ��������caterory}
		    
                    #���Ѿ���������Ŀ���������������Ŀ���ֵ�λ�ý���������
                    #��mostclick�д�ŵ��ǻỰ�ʹ˻Ự��1������������Ŀ
                    break
                clickInfo = {}
        sessionId = data[0]
        if clickInfo.has_key(data[3].strip()):
            clickInfo[data[3].strip()]+=1 #clickInfo����:{itemId1:����,itemId2:����..}}
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
                    number +=1    #�̺��Ŷ�������������Ĺ����buy�е���Ӧ��Session
                totalNumber += 1     ###totalNumber��ʾbuy���ܵ�Session��        
        sessionId= data[0]
    
    print number                   #100271           
    print totalNumber              #509695
    print 1.0*number/totalNumber   #0.196727454654
#���Item��category���ֵ�
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














