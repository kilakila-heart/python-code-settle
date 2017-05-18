# -*- coding: cp936 -*-
import string
import random
import os
from scipy import stats
import numpy as np
def hx(x):
    if x>100:
        return 1.0
    if x<-100:
        return 0.0
    return (1+np.e**(-x))**(-1)
#s1_clickInfo = {itemId1:1;itemid2:1;...}
def jarccardSim(sessionInfo1,sessionInfo2):
    s1_clickInfo = {}
    s2_clickInfo ={}
    for i in range(len(sessionInfo1)):
        s1_clickInfo[sessionInfo1[i]] = 1
    for i in range(len(sessionInfo2)):
        s2_clickInfo[sessionInfo2[i]] = 1
    jDistanceUp = 0
    jDistanceDown = 0
    for itemId in s1_clickInfo:
        if s2_clickInfo.has_key(itemId):
            jDistanceUp +=1
        jDistanceDown += 1
    for itemId in s2_clickInfo:
        if not s1_clickInfo.has_key(itemId):
            jDistanceDown +=1
    return 1.0*jDistanceUp/jDistanceDown
    
def generateExpirienmentData(clickFile,outputFolder):
    file_clicks = open(clickFile)
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)
    file_write = open(outputFolder+"\\four.dat",'w')
    
    for line in file_clicks:
        data = line.split(",")
        month = string.atoi(data[1].split("-")[1])
        if month < 5:
            file_write.write(line)
    file_write.close()
def generateTrainingData(fileName):
    file_clicks = open(fileName)
    file_training = open(fileName+"_training",'w')
    file_test = open(fileName+"_test",'w')
    sessionId = "-1"
    click = {}
    number = 0
    for line in file_clicks:
        data = line.split(",")
        if sessionId != data[0]:
            if sessionId != "-1":
                if len(click)>1:
                    tmpNumber = 0
                    top = (len(click)+1)/2
                    for numberI in click:
                        if tmpNumber<top:
                            file_training.write(click[numberI])
                        else:
                            if string.atoi((click[numberI].split(",")[1].split("-")[2]).split("T")[0]) ==30:
                                file_test.write(click[numberI])
                            else:
                                file_training.write(click[numberI])
                        tmpNumber+=1
            sessionId = data[0]
            click = {}
            number = 0
        click[number] = line
        number+=1
    file_training.close()
    file_test.close()
def generateLastdayClick(clickFile,outputFile,month,day):
    file_clicks = open(clickFile)
    file_out = open(outputFile+"-"+str(month)+"-"+str(day),'w')
    itemClickedNumber = {}
    for line in file_clicks:
        data = line.split(",")
        time = data[1]
        monthNow = string.atoi(time.split("-")[1])
        dayNow = string.atoi((time.split("-")[2]).split("T")[0])
        if monthNow == month and dayNow == day-1:
            if not itemClickedNumber.has_key(data[2]):
                itemClickedNumber[data[2]] = 1
            else:
                itemClickedNumber[data[2]] += 1
    file_out.write(str(itemClickedNumber))
    file_out.close()
#generateLastdayClick('D:\\Data\\expirienment\\four.dat_training','D:\\Data\\expirienment\\',4,30)
    
def preProcess(trainingFile,testFile):
    file_Training = open(trainingFile)
    sessionInfo = {}
    itemInfo = {}
    for line in file_Training:
        data = line.split(",")
        if not sessionInfo.has_key(data[0]):
            sessionInfo[data[0]]=[]
        if not itemInfo.has_key(data[2]):
            itemInfo[data[2]] = []
        itemInfo[data[2]].append(data[0])
        sessionInfo[data[0]].append(data[2])

    file_Test = open(testFile)
    testSessionInfo = {}
    testItemInfo = {}
    for line in file_Test:
        data = line.split(",")
        if not testSessionInfo.has_key(data[0]):
            testSessionInfo[data[0]]=[]
        if not testItemInfo.has_key(data[2]):
            testItemInfo[data[2]] = []
        testItemInfo[data[2]].append(data[0])
        testSessionInfo[data[0]].append(data[2])
    return sessionInfo,itemInfo,testSessionInfo,testItemInfo
def getInfo(fileName):
    fileInfo = open(fileName)
    info = {}
    for line in fileInfo:
        info = eval(line)
        return info

def getTopKSimSession(sessionInfo,itemInfo,sessionId,K):
    simValues = {}
    for itemId in sessionInfo[sessionId]:
        for simSessionId in itemInfo[itemId]:
            if simSessionId == sessionId or simValues.has_key(simSessionId):
                continue
            
            simValue = jarccardSim(sessionInfo[simSessionId],sessionInfo[sessionId])
            simValues[simSessionId] = simValue
    if K>len(simValues):
        K = len(simValues)
    simValues = sorted(simValues.iteritems(),key=lambda s:s[1],reverse=True)
    topkSession = {}
    
    for i in range(K):
        topkSession[simValues[i][0]] = simValues[i][1]
    return topkSession

def clicked(sessionClicked,itemId):
    for i in range(len(sessionClicked)):
        if sessionClicked[i]==itemId:
            return 1
    return 0

def getLastDayClick(fileDic,month,day):
    fileIn = open(fileDic+"-"+str(month)+"-"+str(day))
    lastDayClicked = {}
    for line in fileIn:
        lastDayClicked = eval(line)
        break
    number = 0
    clickedNumber = 0
    maxClick = 0
    for itemId in lastDayClicked:
        number+=1
        if lastDayClicked[itemId]>maxClick:
            maxClick = lastDayClicked[itemId]
        clickedNumber+=lastDayClicked[itemId]
    clickAvg = 1.0*clickedNumber/number
    return lastDayClicked,clickAvg,maxClick

#lastDayClicked,clickAvg = getLastDayClick('D:\\Data\\expirienment\\',4,30)
#print clickAvg
def getGlobalScore(sessionInfo,itemInfo,topkSession,itemId):
    score = 0.0
    for sessionId in topkSession:
        score += topkSession[sessionId]*clicked(sessionInfo[sessionId],itemId)
    return score

def getGlobalScoreRate():
    sessionInfo,itemInfo,testSessionInfo,testItemInfo = preProcess('D:\\Data\\expirienment\\four.dat_training','D:\\Data\\expirienment\\four.dat_test')
    rightChoose = 0
    totalChoose = 0
    for testSessionId in testSessionInfo:
        topkSession = getTopKSimSession(sessionInfo,itemInfo,testSessionId,10)
        itemIds = {}
        for sessionId in topkSession:
            for i in range(len(sessionInfo[sessionId])):
                itemIds[sessionInfo[sessionId][i]] = 1
        for itemId in sessionInfo[testSessionId]:
            itemIds[itemId]  = 1
        totalItems = {}
        for itemId in itemIds:
            totalItems[itemId] = 1
        for itemId in testSessionInfo[testSessionId]:
            totalItems[itemId] = 1
        totalChoose +=len(totalItems)
        rightChoose+= len(itemIds)+len(testSessionInfo[testSessionId])-len(totalItems)
    print totalChoose,rightChoose
def getLocalScore(sessionInfo,itemInfo,testSessionId,itemId):
    if not clicked(sessionInfo[testSessionId],itemId):
        return 0.0
    localScore = 0.0
    for simItemId in sessionInfo[testSessionId]:
        localScore+=jarccardSim(itemInfo[simItemId],itemInfo[itemId])
    return localScore

def getLastdayClick(clickFile,month,day):
    for line in file_clicks:
        data = line.split(",")
        month = string.atoi(data[1].split("-")[1])
        if month < 5:
            file_write.write(line)
    file_write.close()

def test():
    sessionInfo,itemInfo,testSessionInfo,testItemInfo = preProcess('D:\\Data\\expirienment\\four.dat_training','D:\\Data\\expirienment\\four.dat_test')
    number = 0
    for testSessionId in testSessionInfo:
        for itemId in sessionInfo[testSessionId]:
            print testSessionId,itemId,getLocalScore(sessionInfo,itemInfo,testSessionId,itemId)
        print testSessionId,'214753916',getLocalScore(sessionInfo,itemInfo,testSessionId,'214753916')
        number += 1
        if number>5:
            break
def generateFeature():
    sessionInfo,itemInfo,testSessionInfo,testItemInfo = preProcess('D:\\Data\\expirienment\\four.dat_training','D:\\Data\\expirienment\\four.dat_test')
    lastDayClicked,clickAvg,maxClick = getLastDayClick('D:\\Data\\expirienment\\',4,30)
    fileOut = open('D:\\Data\\expirienment\\feature.dat','w')
    right = 0
    notRight = 0
    for testSessionId in testSessionInfo:
        topkSession = getTopKSimSession(sessionInfo,itemInfo,testSessionId,10)
        itemIds = {}
        for sessionId in topkSession:
            for i in range(len(sessionInfo[sessionId])):
                itemIds[sessionInfo[sessionId][i]] = 0
        for itemId in testSessionInfo[testSessionId]:
            itemIds[itemId]  = 1
        for itemId in itemIds:
            globalScore = getGlobalScore(sessionInfo,itemInfo,topkSession,itemId)
            localScore = getLocalScore(sessionInfo,itemInfo,testSessionId,itemId)
            popularityScore = clickAvg/maxClick
            if lastDayClicked.has_key(itemId):
                popularityScore = 1.0*lastDayClicked[itemId]/maxClick
            fileOut.write(str(globalScore)+","+str(localScore)+","+str(popularityScore)+","+str(itemIds[itemId])+"\n")
            if itemIds[itemId]==0:
                notRight +=1
            else:
                right+=1
    fileOut.close()
    print right,notRight
def getFeatureFromFIle(fileName):
    fin = open(fileName)
    X = []
    Y = []
    for line in fin:
        data = line.split(",")
        for i in range(len(data)):
            data[i] = string.atof(data[i])
        Y.append(data[-1])
        data[-1] = 1.0
        X.append(data)
    Theta = [1 for i in range(len(X[0]))]
    return X,Y,Theta
def logicRegression(X,Y,Theta,MAXLOOP,decayRate):
    flagNumber = 0
    maxRate= 0.0
    maxTheta = []
    for mi in range(MAXLOOP):
        if (mi+1)%50==0:
            decayRate /= 2
        loopValue = 0.0
        rightNumber = 0
        totalNumber = 0
        HTheta = [0 for i in range(len(Y))]
        for j in range(len(Y)):
            for k in range(len(X[0])):
                tmpValue = Y[j]-hx(np.dot(Theta,X[j]))
                if -0.5<=tmpValue<=0.5:
                    rightNumber+=1
                totalNumber+=1
                HTheta[k] = HTheta[k]+tmpValue*X[j][k]
                loopValue +=tmpValue
        for k in range(len(X[0])):
            if flagNumber == k:
                Theta[k] = Theta[k] + decayRate*HTheta[k]
        flagNumber +=1
        flagNumber = flagNumber%len(X[0])
        print loopValue,Theta
        nowRate = 1.0*rightNumber/totalNumber
        print nowRate
        if nowRate > maxRate :
            maxTheta = Theta
            maxRate = nowRate
    print "maxTheta:"+str(maxTheta)+",maxRate:"+ str(maxRate)
    return Theta
    

def getLogicRegressionPara():
    X,Y,Theta = getFeatureFromFIle('D:\\Data\\expirienment\\feature.dat')
    Theta = logicRegression(X,Y,Theta,500,0.00001)
    print Theta
def testTheta():
    X,Y,Theta = getFeatureFromFIle('D:\\Data\\expirienment\\feature.dat')
    Theta =  [-0.52498548042472892, 0.69977295598605016, 1.0277526988380215, 0.0074433264408245992]
    rightNumber=0
    totalNumber=0
    for i in range(len(Y)):
        tmpInt = random.randint(0,9)
        if tmpInt ==0:
            predict = hx(np.dot(Theta,X[i]))
            if predict >0.5 and Y[i]== 1:
                rightNumber+=1
            if predict <0.5 and Y[i]== 0:
                rightNumber+=1
            totalNumber+=1
    print rightNumber,totalNumber,1.0*rightNumber/totalNumber
#getLogicRegressionPara()
#generateFeature()
testTheta()



