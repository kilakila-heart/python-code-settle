# -*- coding: cp936 -*-
import string
import math
import numpy as np
import matplotlib.pyplot as plt
import random
#file_object_w = open('D:\Data\information.txt','w')
'''
#生成购买session数量与点击session数量，即看数据的稀疏度
file_object1 = open('D:\Data\yoochoose-buys.dat')
file_object2 = open('D:\Data\yoochoose-clicks.dat')
s1={}
s2={}
for line in file_object1:
    s1[line.split(",")[0]]=1
for line in file_object2:
    s2[line.split(",")[0]]=1
file_object_w.write("购买session数："+str(len(s1))+"\n")
file_object_w.write("点击session数："+str(len(s2))+"\n")
file_object_w.write("数据稀疏度："+str(1.0*len(s1)/len(s2))+"\n")

#生成购买数的分布
file_object3 = open('D:\Data\yoochoose-buys-analyse-sorted.dat')
a = [0 for i in range(5)]
for line in file_object3:
    a[int(math.log(string.atoi(line.split("\t")[1]),10))]+=1
x = [i for i in range(5)]
width = 0.35
menStd =   (2, 3, 4, 1, 2)
fig, ax = plt.subplots()
rects1 = ax.bar(x, a, width, color='r', yerr=menStd)
ax.set_ylabel('Number')
ax.set_title('The number of buys')
ax.set_xticks(x)
ax.set_xticklabels( ('1', '10', '100', '1000', '10000') )
plt.ylim(0)
plt.show()
file_object_w.write("商品购买数量分布：\n")
file_object_w.write("1~10:\t"+str(a[0])+"\n")
file_object_w.write("10~100:\t"+str(a[1])+"\n")
file_object_w.write("100~1000:\t"+str(a[2])+"\n")
file_object_w.write("1000~10000:\t"+str(a[3])+"\n")
file_object_w.write("10000~100000:\t"+str(a[4])+"\n")

#购买中种类的分布
file_object_w.write("购买中种类的分布:"+"\n")
file_object3 = open('D:\Data\yoochoose-buys.dat')
s={}
for line in file_object3:
    line=line.strip('\n')
    data = line.split(",")
    if len(data[4])>5:
    data[4] = "-1"
    if s.has_key(data[4]):
    s[data[4]]+=1
    else:
    s[data[4]]=1
s = sorted(s.iteritems(),key=lambda s:s[0],reverse=False)
for s_ in s:
    file_object_w.write(s_[0]+":\t"+str(s_[1])+"\n")
print 1
#点击中种类的分布
file_object_w.write("点击中种类的分布:"+"\n")
file_object3 = open('D:\Data\yoochoose-clicks.dat')
s={}
for line in file_object3:
    line=line.strip('\n')
    data = line.split(",")
    if len(data[3])>5:
    data[3] = "-1"
    if s.has_key(data[3]):
    s[data[3]]+=1
    else:
    s[data[3]]=1
s = sorted(s.iteritems(),key=lambda s:s[0],reverse=False)
for s_ in s:
    file_object_w.write(s_[0]+":\t"+str(s_[1])+"\n")
print 2
#包含购买的点击中种类分布
file_object_w.write("包含购买的点击中种类分布:"+"\n")
file_object3 = open('D:\Data\yoochoose-clicks-hasBuyData.dat')
s={}
for line in file_object3:
    line=line.strip('\n')
    data = line.split(",")
    if len(data[3])>5:
    data[3] = "-1"
    if s.has_key(data[3]):
    s[data[3]]+=1
    else:
    s[data[3]]=1
s = sorted(s.iteritems(),key=lambda s:s[0],reverse=False)
for s_ in s:
    file_object_w.write(s_[0]+":\t"+str(s_[1])+"\n")
print 3

#购买商品时，点击次数分布
file_object1 = open('D:\Data\yoochoose-buys-sorted.dat')
file_object2 = open('D:\Data\yoochoose-clicks.dat')
s={}
file_object_w.write("购买点击次数的分布:"+"\n")
a = [0 for i in range(100)]
for line in file_object1:
    data = line.split(",")
    s[data[0]+" "+ data[2]] = 0
for line in file_object2:
    data = line.split(",")
    if s.has_key(data[0]+" "+data[2]):
    s[data[0]+" "+data[2]]+=1
for s_ in s:
    if(s[s_]>99):
    print s_+":\t"+str(s[s_])
    else:
    a[s[s_]]+=1
for i in range(100):
    file_object_w.write(str(i)+":\t"+str(a[i])+"\n")

#流行商品(占90%购买数的商品)在点击序列中的分布
file_object_w.write("流行商品(占90%购买数的商品)在点击序列中的分布:"+"\n")
file_object1 = open('D:\Data\yoochoose-buys-analyse-sorted.dat')
file_object2 = open('D:\Data\yoochoose-clicks-hasBuyData.dat')
file_object3 = open('D:\Data\yoochoose-clicks-hasBuyData.dat')
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
a = [0 for i in range(11)]
while True:
    flag = 0
    popularOrNot = 0
    tmpSession = "-1"
    for line in file_object2:
    data = line.split(",")
    if s.has_key(data[2]):
        popularOrNot = 1
    if tmpSession=="-1":
        tmpSession = data[0]
    elif tmpSession!= data[0]:
        break
    flag += 1
    if flag==0:
    break
    flagNumber = 0
    for line in file_object3:
    flagNumber+=1
    if popularOrNot==1 and flag>=10:
        if s.has_key(line.split(",")[2]):
        a[flagNumber*10/flag]+=1
    if flagNumber==flag:
        break
for i in range(11):
    file_object_w.write(str(i)+":\t"+str(a[i])+"\n")


#小于N次点击包含popular的比例
N = 2
file_object1 = open('D:\Data\yoochoose-buys-analyse-sorted.dat')
file_object2 = open('D:\Data\yoochoose-clicks-hasBuyData.dat')
file_object3 = open('D:\Data\yoochoose-clicks-hasBuyData.dat')
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
totalNumber = 0
popularNumber = 0
while True:
    flag = 0
    popularOrNot = 0
    tmpSession = "-1"
    for line in file_object2:
    data = line.split(",")
    if s.has_key(data[2]):
        popularOrNot = 1
    if tmpSession=="-1":
        tmpSession = data[0]
    elif tmpSession!= data[0]:
        break
    flag += 1
    if flag==0:
    break
    totalNumber +=1
    if popularOrNot==1 and flag<=N:
    popularNumber +=1
file_object_w.write("小于等于"+str(N)+"次点击包含popular的比例:"+str(1.0*popularNumber/totalNumber)+"\n")

#时间区间的统计
file_object_w.write("购买发生的时间区间："+"\n")
file_object1 = open('D:\Data\yoochoose-buys.dat')
time = [0 for i in range(24)]
for line in file_object1:
    hour = string.atoi(line.split("T")[1][0:2])
    time[hour]+=1
for i in range(24):
    file_object_w.write(str(i)+"~"+str(i+1)+":\t"+str(time[i])+"\n")

file_object_w.write("点击发生的时间区间："+"\n")
file_object1 = open('D:\Data\yoochoose-clicks.dat')
time = [0 for i in range(24)]
for line in file_object1:
    hour = string.atoi(line.split("T")[1][0:2])
    time[hour]+=1
for i in range(24):
    file_object_w.write(str(i)+"~"+str(i+1)+":\t"+str(time[i])+"\n")

file_object_w.write("包含购买的点击发生的时间区间："+"\n")
file_object1 = open('D:\Data\yoochoose-clicks-hasBuyData.dat')
time = [0 for i in range(24)]
for line in file_object1:
    hour = string.atoi(line.split("T")[1][0:2])
    time[hour]+=1
for i in range(24):
    file_object_w.write(str(i)+"~"+str(i+1)+":\t"+str(time[i])+"\n")


#统计购买与不购买点击的平均长度

file_object1 = open('D:\Data\yoochoose-clicks-hasBuyData.dat')
tmpString = "-1"
number = 0
clickNumber = 0
for line in file_object1:
    clickNumber += 1
    data = line.split(",")
    if data[0] != tmpString:
    number+=1
    tmpString = data[0]

file_object_w.write("包含购买的点击平均长度："+str(1.0*clickNumber/number)+"\n")

file_object1 = open('D:\Data\yoochoose-clicks-notBuyData.dat')
tmpString = "-1"
number = 0
clickNumber = 0
for line in file_object1:
    clickNumber += 1
    data = line.split(",")
    if data[0] != tmpString:
    number+=1
    tmpString = data[0]
file_object_w.write("不包含购买的点击平均长度："+str(1.0*clickNumber/number)+"\n")


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


    
#统计购买点击的时长分布
file_object1 = open('D:\Data\yoochoose-clicks-hasBuyData.dat')
file_object_w.write("统计购买点击的时长分布："+"\n")

beginTime = "-1"
endTime = "-1"
sessionId = "-1"
s={}
flagNumber = 0
for line in file_object1:
    data = line.split(",")
    if sessionId != data[0]:
    if sessionId == "-1":
        beginTime = data[1]
        sessionId = data[0]
    else:
        if flagNumber==1:
        number = 0
        else :number = calculateTime(beginTime,endTime)
        if number==-1:
        print sessionId
        if s.has_key(number):
        s[number]+=1
        else:
        s[number]=1
        beginTime = data[1]
        sessionId = data[0]
    flagNumber = 1
    else:
    endTime = data[1]
    flagNumber +=1
s = sorted(s.iteritems(),key=lambda s:s[0],reverse=False)
number = 0
for s_ in s:
    number += s_[1]
    
for s_ in s:
    file_object_w.write(str(s_[0])+"\t"+str(s_[1])+"\t"+str(1.0*s_[1]/number)+"\n")


#统计非购买的时长分布

file_object1 = open('D:\Data\yoochoose-clicks-notBuyData.dat')
file_object_w.write("统计非购买点击的时长分布："+"\n")

beginTime = "-1"
endTime = "-1"
sessionId = "-1"
s={}
flagNumber = 0
for line in file_object1:
    data = line.split(",")
    if sessionId != data[0]:
    if sessionId == "-1":
        beginTime = data[1]
        sessionId = data[0]
    else:
        if flagNumber==1:
        number = 0
        else :number = calculateTime(beginTime,endTime)
        if number==-1:
        print sessionId
        if s.has_key(number):
        s[number]+=1
        else:
        s[number]=1
        beginTime = data[1]
        sessionId = data[0]
    flagNumber = 1
    else:
    endTime = data[1]
    flagNumber +=1
s = sorted(s.iteritems(),key=lambda s:s[0],reverse=False)
number = 0
for s_ in s:
    number += s_[1]
    
for s_ in s:
    file_object_w.write(str(s_[0])+"\t"+str(s_[1])+"\t"+str(1.0*s_[1]/number)+"\n")



#统计购买日分布
file_object1 = open('D:\Data\yoochoose-buys.dat')
s = {}
for line in file_object1:
    data = line.split(",")
    day = data[1].split("T")[0]
    if s.has_key(day):
    s[day] += 1
    else:
    s[day] = 1
s = sorted(s.iteritems(),key=lambda s:s[0],reverse=False)
month = {}
monthNumber= {}
wn = 1 #4-1是星期2
week = {}
weekNumber = {}
for s_ in s:
    data = s_[0].split("-")
    if month.has_key(data[1]):
    month[data[1]] += s_[1]
    else:
    month[data[1]] = s_[1]
    if monthNumber.has_key(data[1]):
    monthNumber[data[1]] += 1
    else:
    monthNumber[data[1]] = 1
        
    if week.has_key(wn):
    week[wn] += s_[1]
    else:
    week[wn] = s_[1]
    
    if weekNumber.has_key(wn):
    weekNumber[wn] += 1
    else:
    weekNumber[wn] = 1
    wn = (wn+1)% 7
file_object_w.write("统计购买月均日分布："+"\n")
month = sorted(month.iteritems(),key=lambda s:s[0],reverse=False)
for s_ in month:
    file_object_w.write(str(s_[0])+"\t"+str(s_[1]/monthNumber[s_[0]])+"\n")
    
file_object_w.write("统计购买星期平均分布："+"\n")
week = sorted(week.iteritems(),key=lambda s:s[0],reverse=False)
for s_ in week:
    file_object_w.write(str(s_[0]+1)+"\t"+str(s_[1]/weekNumber[s_[0]])+"\n")



#统计点击日分布
file_object1 = open('D:\Data\yoochoose-clicks.dat')
s = {}
for line in file_object1:
    data = line.split(",")
    day = data[1].split("T")[0]
    if s.has_key(day):
    s[day] += 1
    else:
    s[day] = 1
s = sorted(s.iteritems(),key=lambda s:s[0],reverse=False)
month = {}
monthNumber= {}
wn = 1 #4-1是星期2
week = {}
weekNumber = {}
for s_ in s:
    data = s_[0].split("-")
    if month.has_key(data[1]):
    month[data[1]] += s_[1]
    else:
    month[data[1]] = s_[1]
    if monthNumber.has_key(data[1]):
    monthNumber[data[1]] += 1
    else:
    monthNumber[data[1]] = 1
        
    if week.has_key(wn):
    week[wn] += s_[1]
    else:
    week[wn] = s_[1]
    
    if weekNumber.has_key(wn):
    weekNumber[wn] += 1
    else:
    weekNumber[wn] = 1
    wn = (wn+1)% 7
file_object_w.write("统计点击月均日分布："+"\n")
month = sorted(month.iteritems(),key=lambda s:s[0],reverse=False)
for s_ in month:
    file_object_w.write(str(s_[0])+"\t"+str(s_[1]/monthNumber[s_[0]])+"\n")
    
file_object_w.write("统计点击星期平均分布："+"\n")
week = sorted(week.iteritems(),key=lambda s:s[0],reverse=False)
for s_ in week:
    file_object_w.write(str(s_[0]+1)+"\t"+str(s_[1]/weekNumber[s_[0]])+"\n")

#统计星期平均点击购买比
file_object1 = open('D:\Data\yoochoose-buys.dat')
s = {}
for line in file_object1:
    data = line.split(",")
    day = data[1].split("T")[0]
    if s.has_key(day):
    s[day] += 1
    else:
    s[day] = 1
s = sorted(s.iteritems(),key=lambda s:s[0],reverse=False)
wn = 1 #4-1是星期2
week = {}
for s_ in s:
    data = s_[0].split("-")     
    if week.has_key(wn):
    week[wn] += s_[1]
    else:
    week[wn] = s_[1]
    wn = (wn+1)% 7
week = sorted(week.iteritems(),key=lambda s:s[0],reverse=False)
file_object1 = open('D:\Data\yoochoose-clicks-hasBuyData.dat')
s = {}
for line in file_object1:
    data = line.split(",")
    day = data[1].split("T")[0]
    if s.has_key(day):
    s[day] += 1
    else:
    s[day] = 1
s = sorted(s.iteritems(),key=lambda s:s[0],reverse=False)
wn = 1 #4-1是星期2
week_click = {}
for s_ in s:
    data = s_[0].split("-")     
    if week_click.has_key(wn):
    week_click[wn] += s_[1]
    else:
    week_click[wn] = s_[1]
    wn = (wn+1)% 7
file_object_w.write("统计星期日的购买点击比："+"\n")
for s_ in week:
    file_object_w.write(str(s_[0]+1)+"\t"+str(1.0*week_click[s_[0]]/s_[1])+"\n")

file_object_w.close()

#根据分类结果输出solution.dat
file_feature = open('D:\Data\yoochoose-predict.dat')
file_out = open('D:\Data\solution.dat','w')
for line in file_feature:
    data = line.split(",")
    if(data[1].strip()=="yes"):
    file_out.write(data[0]+":\n")
file_out.close()

#随机产生1/10的结果
file_feature = open('D:\Data\yoochoose-predict.dat')
file_out = open('D:\Data\solution-random.dat','w')
for line in file_feature:
    number = random.randint(0,9)
    data = line.split(",")
    if(number==0):
    file_out.write(data[0]+":\n")
file_out.close()
'''
#根据决策和随机得到的答案分别再在购买选项中随机选取购买的Item
'''
file_feature = open('D:\Data\solution\solution-random1.dat')
file_out = open('D:\Data\solution\\random-random.dat','w')
buys = {}
for line in file_feature:
    buys[line.split(":")[0]] = 1
file_click = open('D:\Data\yoochoose-test.dat')
sessionId = "-1"
items = []
for line in file_click:
    data = line.split(",")
    if data[0]!=sessionId:
    if sessionId !=  "-1":
        tmpNumber = random.randint(0,len(items)-1)
        if(tmpNumber==0):
        file_out.write(sessionId+":"+items[tmpNumber]+"\n")
    items = []
    sessionId = data[0]
    items.append(data[2])
file_out.close()
'''

#生成答案文件
def getAnswerFile(featureFile,outFile):
    file_feature = open(featureFile)
    file_out = open(outFile,'w')
    buys = {}
    for line in file_feature:
        data = line.split(",")
        if data[1].strip() == "yes":
            buys[data[0]] = 1
    file_click = open('D:\Data\yoochoose-test.dat')
    sessionId = "-1"
    clickInfo = {}
    items = []
    for line in file_click:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                clickInfo = sorted(clickInfo.iteritems(),key=lambda s:s[1],reverse=True)
                for clickInfo_ in clickInfo:
                    if buys.has_key(sessionId):
                        file_out.write(sessionId+";"+clickInfo_[0]+"\n")#clickInfo_[0]+
                        break
            clickInfo = {}
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]]+=1
        else:
            clickInfo[data[2]] = 1
        sessionId = data[0]
    file_out.close()
'''
#生成训练集和测试集
file_balance = open('D:\Data\yoochoose-clicks-feature-balence.dat')
file_out1 = open('D:\Data\data\\training-balance.dat','w')
file_out2 = open('D:\Data\data\\test-balence.dat','w')

number = 0
for line in file_balance:
    if number==0:
    file_out2.write(line)
    file_out1.write(line)
    elif number%10 ==0:
    file_out2.write(line)
    else:
    file_out1.write(line)
    number+=1
file_out1.close()
file_out2.close()

#根据session排序yoochoose-clicks-hasBuyData
file_balance = open('D:\Data\yoochoose-clicks-hasBuyData.dat')
file_out1 = open('D:\Data\yoochoose-clicks-hasBuyData-sorted','w')
s={}
for line in file_balance:
    sessionId = string.atoi(line.split(",")[0])
    s[line] = sessionId
s = sorted(s.iteritems(),key=lambda s:s[1],reverse=False)
for s_ in s:
    file_out1.write(s_[0])
file_out1.close()
'''
#根据20个预测文件生成答案文件
def getLastSolutionFromMany(rRate):
    recieveRate = rRate
    file_out = open('D:\Data\solution\\lastSolution-noWeekTime\\decision-most-recieve-'+str(recieveRate)+'-17.dat','w')
    buys = {}
    totalBuys = {}

    testNumber = 0

    for i in range(17):
        file_read = open('D:\Data\\solution\\oneSolution-noWeekTime\\solution'+str(i)+'.dat')
        for line in file_read:
            if i==0:
                testNumber +=1
            data = line.split(",")
            if data[1].strip() == "yes":
                if totalBuys.has_key(data[0]):
                    totalBuys[data[0]] += 1
                else:
                    totalBuys[data[0]] = 1
    totalBuys = sorted(totalBuys.iteritems(),key=lambda s:s[1],reverse=True)
    recieveNumber = int(testNumber*recieveRate)
    print recieveNumber
    for buysInfo in totalBuys:
        if recieveNumber==0:
            break
        recieveNumber-=1
        buys[buysInfo[0]] = 1
    print len(buys)
    file_click = open('D:\Data\yoochoose-test.dat')
    sessionId = "-1"
    clickInfo = {}
    items = []
    for line in file_click:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                clickInfo = sorted(clickInfo.iteritems(),key=lambda s:s[1],reverse=True)
                for clickInfo_ in clickInfo:
                    if buys.has_key(sessionId):
                        file_out.write(sessionId+";"+clickInfo_[0]+"\n")#clickInfo_[0]+
                    break
                clickInfo = {}
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]]+=1
        else:
            clickInfo[data[2]] = 1
        sessionId = data[0]
    file_out.close()
def getAllRecieve():
    file_out = open('D:\Data\solution\\lastSolution\\allRecieve.dat','w')

    file_click = open('D:\Data\yoochoose-test.dat')
    sessionId = "-1"
    clickInfo = {}
    items = []
    for line in file_click:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                clickInfo = sorted(clickInfo.iteritems(),key=lambda s:s[1],reverse=True)
                for clickInfo_ in clickInfo:
                    file_out.write(sessionId+";"+clickInfo_[0]+"\n")#clickInfo_[0]+
                    break
                clickInfo = {}
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]]+=1
        else:
            clickInfo[data[2]] = 1
        sessionId = data[0]
    file_out.close()
def getLastSolutionFromManyPerThousand(rRate):
    recieveRate = rRate
    file_out = open('D:\Data\solution\\lastSolution-noWeekTime\\decision-most-recieve-'+str(recieveRate)+'-PerThousand.dat','w')
    buys = {}
    totalBuys = {}
    testNumber = 0
    for i in range(17):
        file_read = open('D:\Data\\solution\\oneSolution-noWeekTime\\solution'+str(i)+'.dat')
        for line in file_read:
            if i==0:
                testNumber +=1
            data = line.split(",")
            if data[1].strip() == "yes":
                if totalBuys.has_key(data[0]):
                    totalBuys[string.atoi(data[0])] += 1
                else:
                    totalBuys[string.atoi(data[0])] = 1
    totalBuys = sorted(totalBuys.iteritems(),key=lambda s:s[0],reverse=False)
    choosedBuys = {}
    number = 1
    for buysInfo in totalBuys:
        if buysInfo[0]>number*5000:
            choosedBuys = sorted(choosedBuys.iteritems(),key=lambda s:s[1],reverse=True)
            choosedBuysNumber = 1000*rRate
            for b_ in choosedBuys:
                buys[b_[0]] = 1
                choosedBuysNumber-=1
                if choosedBuysNumber ==0:
                    break
            choosedBuys = {}
            number+=1
        choosedBuys[buysInfo[0]] = buysInfo[1]
    print len(buys)
    file_click = open('D:\Data\yoochoose-test.dat')
    sessionId = "-1"
    clickInfo = {}
    items = []
    for line in file_click:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                clickInfo = sorted(clickInfo.iteritems(),key=lambda s:s[1],reverse=True)
                for clickInfo_ in clickInfo:
                    if buys.has_key(string.atoi(sessionId)):
                        file_out.write(sessionId+";"+clickInfo_[0]+"\n")#clickInfo_[0]+
                    break
                clickInfo = {}
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]]+=1
        else:
            clickInfo[data[2]] = 1
        sessionId = data[0]
    file_out.close()
def getTestSessionIds(testSessionFile):
    sessionIds = []
    file_read = open(testSessionFile)
    number = 0
    for line in file_read:
        if number !=0:
            sessionIds.append(line.strip())
        number+=1
    return sessionIds
def getLastSolutionFromWeka(rRate,inputFile,outputFile):
    file_out = open(outputFile,'w')
    file_read = open(inputFile)
    sessionIds = getTestSessionIds('D:\Data\\feature\\yoochoose-test-sessionId.dat')
    start = -1
    recieveRate = rRate
    buys = {}
    for line in file_read:
        if line.find("inst#")!=-1:
            start = 0
            continue
        if start == -1:
            continue
        if len(line)>5:
            data = (line.split(":")[2]).split("       ")
            answer = data[0]
            rate = string.atof(data[1])
            if answer=="yes" and rate > recieveRate:
                buys[sessionIds[start]] = 1
            start +=1
    file_click = open('D:\Data\yoochoose-test.dat')
    sessionId = "-1"
    clickInfo = {}
    items = []
    for line in file_click:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                clickInfo = sorted(clickInfo.iteritems(),key=lambda s:s[1],reverse=True)
                for clickInfo_ in clickInfo:
                    if buys.has_key(sessionId):
                        file_out.write(sessionId+";"+clickInfo_[0]+"\n")#clickInfo_[0]+
                        break
            clickInfo = {}
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]]+=1
        else:
            clickInfo[data[2]] = 1
        sessionId = data[0]
    file_out.close()
def getLastSolutionFromWekaTopK(rRate,inputFile,outputFile,K):
    file_out = open(outputFile,'w')
    file_read = open(inputFile)
    sessionIds = getTestSessionIds('D:\Data\\feature\\yoochoose-test-sessionId.dat')
    start = -1
    recieveRate = rRate
    buys = {}
    for line in file_read:
        if line.find("inst#")!=-1:
            start = 0
            continue
        if start == -1:
            continue
        if len(line)>5:
            data = (line.split(":")[2]).split("       ")
            answer = data[0]
            rate = string.atof(data[1])
            if answer=="yes" and rate > recieveRate:
                buys[sessionIds[start]] = 1
            start +=1
    file_click = open('D:\Data\yoochoose-test.dat')
    sessionId = "-1"
    clickInfo = {}
    eachNumber = 0
    oneNumberBuy = 0
    oneNumberAll = 0
    items = []
    for line in file_click:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                if eachNumber==1:
                    oneNumberAll+=1
                if buys.has_key(sessionId):
                    if eachNumber==1:
                        oneNumberBuy+=1
                    outString = sessionId+";";
                    clickInfo = sorted(clickInfo.iteritems(),key=lambda s:s[1],reverse=True)
                    choosedNumber = 0
                    for clickInfo_ in clickInfo:
                        if choosedNumber==0 or clickInfo_[0]>1:
                            if choosedNumber==0:
                                outString+=clickInfo_[0]
                            else:
                                outString+=","+clickInfo_[0]
                            choosedNumber +=1
                            if choosedNumber==K:
                                break
                    file_out.write(outString+"\n")
            clickInfo = {}
            eachNumber = 0
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]]+=1
        else:
            clickInfo[data[2]] = 1
        sessionId = data[0]
        eachNumber += 1
    print [oneNumberBuy,oneNumberAll,1.0*oneNumberBuy/oneNumberAll] #[5, 314545, 1.589597672829007e-05]
    file_out.close()
def getLastSolutionFromWekaAllTopK(rRate,inputFile,outputFile,K):
    file_out = open(outputFile,'w')
    file_read = open(inputFile)
    sessionIds = getTestSessionIds('D:\Data\\feature\\yoochoose-test-sessionId.dat')
    start = -1
    recieveRate = rRate
    eachNumber = 0
    oneNumberBuy = 0
    oneNumberAll = 0
    buys = {}
    for line in file_read:
        if line.find("inst#")!=-1:
            start = 0
            continue
        if start == -1:
            continue
        if len(line)>5:
            data = (line.split(":")[2]).split("       ")
            answer = data[0]
            rate = string.atof(data[1])
            if answer=="yes" and rate > recieveRate:
                buys[sessionIds[start]] = 1
            start +=1
    file_click = open('D:\Data\yoochoose-test.dat')
    sessionId = "-1"
    clickInfo = {}
    items = []
    for line in file_click:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                if eachNumber==1:
                    oneNumberAll+=1
                if buys.has_key(sessionId):
                    if eachNumber==1:
                        oneNumberBuy+=1
                    outString = sessionId+";";
                    clickInfo = sorted(clickInfo.iteritems(),key=lambda s:s[1],reverse=True)
                    choosedNumber = 0
                    for clickInfo_ in clickInfo:
                        if choosedNumber==0 or clickInfo_[0]>1:
                            if choosedNumber==0:
                                outString+=clickInfo_[0]
                            else:
                                outString+=","+clickInfo_[0]
                            choosedNumber +=1
                            if choosedNumber==K:
                                break
                    file_out.write(outString+"\n")
            clickInfo = {}
            eachNumber=0
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]]+=1
        else:
            clickInfo[data[2]] = 1
        sessionId = data[0]
        eachNumber += 1
    print [oneNumberBuy,oneNumberAll,1.0*oneNumberBuy/oneNumberAll] #[5, 314545, 1.589597672829007e-05]
    file_out.close()
def getDicFromFile(fileName):
    file_in = open(fileName)
    dicInfo = {}
    for line in file_in:
        dicInfo = eval(line)
        break
    return dicInfo

def getBuysFrequentness(buyFile):
    buysFrequentnessFile = open(buyFile)
    buysFrequentness = {}
    for line in buysFrequentnessFile:
        data = line.split("\t")
        buysFrequentness[data[0]] = string.atoi(data[1])
    return buysFrequentness
def getLastSolutionFromWekaTopKAllOne(rRate,inputFile,outputFile,K,buysRate,MINCLICK):
    file_out = open(outputFile+"-"+str(K)+"-"+str(buysRate)+"-"+str(MINCLICK)+".dat",'w')
    file_read = open(inputFile)
    sessionIds = getTestSessionIds('D:\Data\\feature\\yoochoose-test-sessionId.dat')
    buysFrequentness = getBuysFrequentness('D:\Data\yoochoose-buys-analyse-sorted.dat')
    start = -1
    recieveRate = rRate
    buys = {}
    for line in file_read:
        if line.find("inst#")!=-1:
            start = 0
            continue
        if start == -1:
            continue
        if len(line)>5:
            data = (line.split(":")[2]).split("       ")
            answer = data[0]
            rate = string.atof(data[1])
            if answer=="yes" and rate > recieveRate:
                buys[sessionIds[start]] = 1
            start +=1
    file_click = open('D:\Data\yoochoose-test.dat')
    sessionId = "-1"
    itemId = "-1"
    clickInfo = {}
    oneClickBuysRate = getDicFromFile('D:\Data\yoochoose-buysRate-oneClick.dat')
    eachNumber = 0
    oneNumberBuy = 0
    oneNumberAll = 0
    items = []
    for line in file_click:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                if eachNumber==1:
                    oneNumberAll+=1
                    if oneClickBuysRate.has_key(itemId) and oneClickBuysRate[itemId]>buysRate:
                        buys[sessionId] = 1
                    #if buysFrequentness.has_key(itemId) and buysFrequentness[itemId]>10:
                    #    buys[sessionId] = 1
                if buys.has_key(sessionId):
                    if eachNumber==1:
                        oneNumberBuy+=1
                    outString = sessionId+";";
                    clickInfo = sorted(clickInfo.iteritems(),key=lambda s:s[1],reverse=True)
                    choosedNumber = 0
                    if eachNumber==1:
                        outString+=clickInfo_[0][0]
                    else:
                        for clickInfo_ in clickInfo:
                            if clickInfo_[1]>1 and buysFrequentness.has_key(clickInfo_[0]) and buysFrequentness[clickInfo_[0]] > MINCLICK:
                                if choosedNumber==0:
                                    outString+=clickInfo_[0]
                                else:
                                    outString+=","+clickInfo_[0]
                                choosedNumber +=1
                                if choosedNumber==K:
                                    break
                    if outString!=(sessionId+";") :
                        file_out.write(outString+"\n")
            clickInfo = {}
            eachNumber = 0
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]]+=1
        else:
            clickInfo[data[2]] = 1
        sessionId = data[0]
        itemId = data[2]
        eachNumber += 1
    print [oneNumberBuy,oneNumberAll,1.0*oneNumberBuy/oneNumberAll] #[5, 314545, 1.589597672829007e-05]
    file_out.close()
def getResultFromForm(K,MINCLICK,buysRate,outFile):#33764.7
    buys = {}
    file_out = open(outFile+str(K)+"-"+str(MINCLICK)+"-"+str(buysRate),'w')
    buysFrequentness = getBuysFrequentness('D:\Data\yoochoose-buys-analyse-sorted.dat')
    file_test = open('D:\Data\yoochoose-test.dat')
    sessionId = "-1"
    itemId = "-1"
    clickInfo = {}
    oneClickBuysRate = getDicFromFile('D:\Data\yoochoose-buysRate-oneClick.dat')
    eachNumber = 0
    oneNumberBuy = 0
    oneNumberAll = 0
    items = []
    repeat = 0
    for line in file_test:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                if eachNumber==1:
                    oneNumberAll+=1
                    if oneClickBuysRate.has_key(itemId) and oneClickBuysRate[itemId]>buysRate and buysFrequentness.has_key(itemId) and buysFrequentness[itemId]>10:
                        buys[sessionId] = 1
                    #if buysFrequentness.has_key(itemId) and buysFrequentness[itemId]>10:
                    #    buys[sessionId] = 1
                if repeat==1:
                    buys[sessionId] = 1
                if buys.has_key(sessionId):
                    outString = sessionId+";";
                    clickInfo = sorted(clickInfo.iteritems(),key=lambda s:s[1],reverse=True)
                    choosedNumber = 0
                    if eachNumber == 1:
                        outString+=clickInfo_[0][0]
                        oneNumberBuy+=1
                    else:
                        for clickInfo_ in clickInfo:
                            if clickInfo_[1]>1 and buysFrequentness.has_key(clickInfo_[0]) and buysFrequentness[clickInfo_[0]] > MINCLICK:
                                if choosedNumber==0:
                                    outString+=clickInfo_[0]
                                else:
                                    outString+=","+clickInfo_[0]
                                choosedNumber +=1
                                if choosedNumber==K:
                                    break
                    if outString!=(sessionId+";") :
                        file_out.write(outString+"\n")
            clickInfo = {}
            eachNumber = 0
            repeat =0
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]]+=1
            repeat = 1
        else:
            clickInfo[data[2]] = 1
        sessionId = data[0]
        itemId = data[2]
        eachNumber += 1
    print [oneNumberBuy,oneNumberAll,1.0*oneNumberBuy/oneNumberAll] #[5, 314545, 1.589597672829007e-05]
    file_out.close()
def getRandomResult(K,MINCLICK,buysRate,outFile):
    file_out = open(outFile+str(K)+"-"+str(MINCLICK)+"-"+str(buysRate),'w')
    sessionId = "-1"
    file_test = open('D:\Data\yoochoose-test.dat')
    buysFrequentness = getBuysFrequentness('D:\Data\yoochoose-buys-analyse-sorted.dat')
    for line in file_test:
        data = line.split(",")
        if data[0]!=sessionId:
            flag = random.randint(0,20)
            if sessionId !=  "-1" and flag==1:
                if True:
                    outString = sessionId+";";
                    clickInfo = sorted(clickInfo.iteritems(),key=lambda s:s[1],reverse=True)
                    choosedNumber = 0
                    for clickInfo_ in clickInfo:
                        if clickInfo_[1]>1:
                            if choosedNumber==0:
                                outString+=clickInfo_[0]
                            else:
                                outString+=","+clickInfo_[0]
                            choosedNumber +=1
                            if choosedNumber==K:
                                break
                    if outString!=(sessionId+";") :
                        file_out.write(outString+"\n")
            clickInfo = {}
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]]+=1
            repeat = 1
        else:
            clickInfo[data[2]] = 1
        sessionId = data[0]
    file_out.close()
    
def combineTwoFiles(file1,file2,outfile,kind):
    file_out = open(outfile+"-"+str(kind)+".dat",'w')
    file1Dic = {}
    filein1 = open(file1)
    for line in filein1:
        file1Dic[line] = 1
    filein2 = open(file2)
    if kind=="and":
        for line in filein2:
            if file1Dic.has_key(line):
                file1Dic[line] = 0
        for index in file1Dic:
            if file1Dic[index]==0:
                file_out.write(index)
    elif kind =="or":
        for line in filein2:
            file1Dic[line]  = 1
        for index in file1Dic:
            file_out.write(index)
    elif kind=="minus":
        for line in filein2:
            file1Dic[line]  = 0
        for index in file1Dic:
            if file1Dic[index]==1:
                file_out.write(index)
    file_out.close()

def generateNewClicks():
    file_buys = open('D:\Data\yoochoose-buys.dat')
    itemPriceMax = {} #item最高价格
    itemPriceMin = {} #item最低价格
    itemBuysNumber = {} #item被购买过多少次
    buyInfo = {} #购买session+itemID
    buySession = {} #购买的session
    for line in file_buys:
        data = line.split(",")
        sessionId = data[0]
        time = data[1]
        itemId = data[2]
        price = string.atoi(data[3])
        buyInfo[sessionId+"_"+itemId] = 1
        buySession[sessionId] = 1
        if itemBuysNumber.has_key(itemId):
            itemBuysNumber[itemId] += string.atoi(data[4])
        else:
            itemBuysNumber[itemId] = string.atoi(data[4])            
        if itemPriceMax.has_key(itemId):
            if itemPriceMax[itemId] < price:
                itemPriceMax[itemId] = price
        else:
            itemPriceMax[itemId] = price
        if itemPriceMin.has_key(itemId):
            if itemPriceMin[itemId] > price and price!=0:
                itemPriceMin[itemId] = price
        else:
            itemPriceMin[itemId] = price
    file_clicks = open('D:\Data\yoochoose-clicks-small.dat')
    file_newcClicks = open('D:\Data\yoochoose-newClicks.dat','w')
    for line in file_clicks:
        data = line.split(",")
        sessionId = data[0]
        time = data[1]
        itemId = data[2]
        buyOrNot = -1 #-1表示没买，0表示session购买了但没购买该Item
        maxPrice = -1 
        minPrice = -1
        itemNumber = -1
        if itemBuysNumber.has_key(itemId):
            itemNumber = itemBuysNumber[itemId]
        if itemPriceMax.has_key(itemId):
            maxPrice = itemPriceMax[itemId]
        if itemPriceMin.has_key(itemId):
            minPrice = itemPriceMin[itemId]
        if buySession.has_key(sessionId):
            buyOrNot = 0
            if buyInfo.has_key(sessionId+"_"+itemId):
                buyOrNot = buyInfo[sessionId+"_"+itemId]
        file_newcClicks.write(str(buyOrNot)+"\t"+
                              str(minPrice)+"\t"+
                              str(maxPrice)+"\t"+
                              str(itemNumber)+"\t"+
                              line)
    file_newcClicks.close()

'''
Rule1: 
'''
def getResultFromFormRule3(K,MINCLICK,buysRate,outFile):#33764.7
    buys = {}
    file_out = open(outFile+str(K)+"-"+str(MINCLICK)+"-"+str(buysRate),'w')
    buysFrequentness = getBuysFrequentness('D:\Data\yoochoose-buys-analyse-sorted.dat')
    file_test = open('D:\Data\yoochoose-test.dat')
    sessionId = "-1"
    itemId = "-1"
    clickInfo = {}
    oneClickBuysRate = getDicFromFile('D:\Data\yoochoose-buysRate-oneClick.dat')
    eachNumber = 0
    oneNumberBuy = 0
    oneNumberAll = 0
    items = []
    repeat = 0
    for line in file_test:
        data = line.split(",")
        if data[0]!=sessionId:
            if sessionId !=  "-1":
                if eachNumber==1:
                    oneNumberAll+=1
                    if oneClickBuysRate.has_key(itemId) and oneClickBuysRate[itemId]>buysRate and buysFrequentness.has_key(itemId) and buysFrequentness[itemId]>10:
                        buys[sessionId] = 1
                    #if buysFrequentness.has_key(itemId) and buysFrequentness[itemId]>10:
                    #    buys[sessionId] = 1
                if repeat==1:
                    buys[sessionId] = 1
                if buys.has_key(sessionId):
                    outString = sessionId+";";
                    clickInfo = sorted(clickInfo.iteritems(),key=lambda s:s[1],reverse=True)
                    choosedNumber = 0
                    if eachNumber == 1:
                        outString+=clickInfo_[0][0]
                        oneNumberBuy+=1
                    else:
                        for clickInfo_ in clickInfo:
                            if clickInfo_[1]>1 and buysFrequentness.has_key(clickInfo_[0]) and buysFrequentness[clickInfo_[0]] > MINCLICK:
                                if choosedNumber==0:
                                    outString+=clickInfo_[0]
                                else:
                                    outString+=","+clickInfo_[0]
                                choosedNumber +=1
                                if choosedNumber==K:
                                    break
                    if outString!=(sessionId+";") :
                        file_out.write(outString+"\n")
            clickInfo = {}
            eachNumber = 0
            repeat =0
        if clickInfo.has_key(data[2]):
            clickInfo[data[2]]+=1
            repeat = 1
        else:
            clickInfo[data[2]] = 1
        sessionId = data[0]
        itemId = data[2]
        eachNumber += 1
    print [oneNumberBuy,oneNumberAll,1.0*oneNumberBuy/oneNumberAll] #[5, 314545, 1.589597672829007e-05]
    file_out.close()




#getResultFromForm(10,10,0.05,"D:\Data\solution\\lastSolution-form\\")#K,MINCLICK,buysRate 33764.7
#getResultFromForm(20,20,0.05,"D:\Data\solution\\lastSolution-form\\") #33609.8
#getAnswerFile('D:\Data\\solution\\oneSolution-noWeekTime\\solution0.dat'
#              ,'D:\Data\solution\\lastSolution-noWeekTime\\decision-most.dat')
#getLastSolutionFromMany(0.35)
#getLastSolutionFromWeka(0.6,'D:\Data\\solution\\wekaResult\\categoryValue.result','D:\Data\solution\\lastSolution-weka\\decision-most-categoryValue-recieve-0.6.dat')
#getLastSolutionFromWekaTopK(0.55,'D:\Data\\solution\\wekaResult\\buysFrequentness.result',
#                            'D:\Data\solution\\lastSolution-weka\\decision-most-buysFrequentness-0.55-K-10.dat',10)

#getLastSolutionFromWekaTopKAllOne(0.55,'D:\Data\\solution\\wekaResult\\buysFrequentness.result',
#                'D:\Data\solution\\lastSolution-weka\\decision-most-',10,0.05,10) #K,buysRate,MINCLICK#33716.9
#generateBuysSession('D:\Data\yoochoose-buys.dat','D:\Data\yoochoose-buys-info.dat')
#combineTwoFiles('D:\Data\solution\\lastSolution-weka\\decision-most--10-0.05-10.dat',"D:\Data\solution\\lastSolution-form\\10-10-0.05",
#                "D:\Data\solution\\lastSolution-combine\\",'and') #33716.9
#combineTwoFiles('D:\Data\solution\\lastSolution-weka\\decision-most--10-0.05-10.dat',"D:\Data\solution\\lastSolution-form\\10-10-0.05",
#                "D:\Data\solution\\lastSolution-combine\\",'or')
#combineTwoFiles("D:\Data\solution\\lastSolution-form\\10-10-0.05",'D:\Data\solution\\lastSolution-weka\\decision-most--10-0.05-10.dat',
#                "D:\Data\solution\\lastSolution-combine\\",'minus')
#getRandomResult(10,10,0.05,"D:\Data\solution\\lastSolution-random\\")
#generateNewClicks()
#getLastSolutionFromWekaTopKAllOne(0.5,'D:\Data\\solution\\wekaResult\\monthLen.result',
#                'D:\Data\solution\\lastSolution-weka\\decision-most-monthLen-0.55-',10,0.05,10)
#getLastSolutionFromWekaTopKAllOne(0.55,'D:\Data\\solution\\wekaResult\\monthLen.result',
#                'D:\Data\solution\\lastSolution-weka\\decision-most-monthLen-0.6-',10,0.05,10)
#getLastSolutionFromWekaTopKAllOne(0.6,'D:\Data\\solution\\wekaResult\\monthLen.result',
#                'D:\Data\solution\\lastSolution-weka\\decision-most-monthLen-0.5-',10,0.05,10)
