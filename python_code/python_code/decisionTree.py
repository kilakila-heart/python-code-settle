# -*- coding: cp936 -*-
import string
import math
import numpy as np
import matplotlib.pyplot as plt
#定义数据集
def getTestDataSet(testDataFile): 
    file_feature = open(testDataFile)
    dataSet = []
    answers = []
    number = 0
    for line in file_feature:
        if number==0:
            data = line.split(",")
            data[-1] = data[-1].strip()
            features = data[:-1]
            print features
              
        else:
            data = line.split(",")
            data[-1] = data[-1].strip()
            data = data[:-1]
            if string.atoi(data[0])<5:
                data[0] = 0
            else:
                data[0] = 1
            if((number+1) %100000 ==0):
                print data
                print number
            dataSet.append(data)
        number+=1
    #print dataSet
    #print features
    #dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]  
    #features = ['no surfacing','flippers']  
    return dataSet,features
    
def createDataSet(fileName): 
    file_feature = open(fileName)
    dataSet = []
    number = 0
    for line in file_feature:
        
        if number==0:
            data = line.split(",")
            features = data[0:-1]
            print features
              
        else:
            data = line.split(",")
            data[-1] = data[-1].strip()
            if string.atoi(data[0])<5:
                data[0] = 0
            else:
                data[0] = 1
            if(number %100000 ==0):
                print data
                print number
            dataSet.append(data)
        number+=1
    #print dataSet
    #print features
    #dataSet = [[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]  
    #features = ['no surfacing','flippers']  
    return dataSet,features

#根据多数原则，从决策中选取一个分类（这里可以换成按概率返回分类）
def classify(classList):  
    ''''' 
    find the most in the set 
    '''
    recieveRate = 0.5
    classCount = {}  
    for vote in classList:  
        if vote not in classCount.keys():  
            classCount[vote] = 0  
        classCount[vote] += 1  
    sortedClassCount = sorted(classCount.iteritems(),key =lambda s:s[1],reverse = True)
    if sortedClassCount[0][0]=="yes":
        rightRate = 1.0*sortedClassCount[0][1]/(sortedClassCount[0][1] +sortedClassCount[1][1])
        if rightRate>recieveRate:
            return "yes"
        else:
            return "no"
    else:
        rightRate = 1.0*sortedClassCount[0][1]/(sortedClassCount[0][1] +sortedClassCount[1][1])
        if rightRate>(1-recieveRate):
            return "no"
        else:
            return "yes"
#计算数据集的殇
def calcShannonEnt(dataset):  
    numEntries = len(dataset)  
    labelCounts = {}  
    for featVec in dataset:  
        currentLabel = featVec[-1]  
        if currentLabel not in labelCounts.keys():  
            labelCounts[currentLabel] = 0  
        labelCounts[currentLabel] += 1  
    shannonEnt = 0.0  
  
    for key in labelCounts:  
        prob = float(labelCounts[key])/numEntries  
        if prob != 0:  
            shannonEnt -= prob*math.log(prob,2)  
    return shannonEnt
#分裂数据集
def splitDataSet(dataset,feat,values):  
    retDataSet = []  
    for featVec in dataset:  
        if featVec[feat] == values:  
            reducedFeatVec = featVec[:feat]  
            reducedFeatVec.extend(featVec[feat+1:])  
            retDataSet.append(reducedFeatVec)  
    return retDataSet  
#寻找最佳分裂属性
def findBestSplit(dataset):  
    numFeatures = len(dataset[0])-1  
    baseEntropy = calcShannonEnt(dataset)  
    bestInfoGain = -111110.0  
    bestFeat = -1  
    for i in range(numFeatures):
        featValues = [example[i] for example in dataset]
        uniqueFeatValues = set(featValues)
        newEntropy = 0.0  
        for val in uniqueFeatValues:
            subDataSet = splitDataSet(dataset,i,val)  
            prob = len(subDataSet)/float(len(dataset))  
            newEntropy += prob*calcShannonEnt(subDataSet)  
        if(baseEntropy - newEntropy)>bestInfoGain:  
            bestInfoGain = baseEntropy - newEntropy  
            bestFeat = i  
    return bestFeat  

#
def treeGrowth(dataSet,features):
    classList = [example[-1] for example in dataSet]  
    if classList.count(classList[0])==len(classList):  
        return classList[0]  
    if len(dataSet[0])==1:# no more features  
        return classify(classList)  
     
    bestFeat = findBestSplit(dataSet)#bestFeat is the index of best feature
    bestFeatLabel = features[bestFeat]
    myTree = {bestFeatLabel:{}}  
    featValues = [example[bestFeat] for example in dataSet]  
    uniqueFeatValues = set(featValues)
    #print bestFeatLabel + str(uniqueFeatValues)+str(bestFeat)+str(features)
    del (features[bestFeat])  
    for values in uniqueFeatValues:  
        subDataSet = splitDataSet(dataSet,bestFeat,values)  
        myTree[bestFeatLabel][values] = treeGrowth(subDataSet,features)  
    features.insert(bestFeat, bestFeatLabel)  
    return myTree



def predict(tree,newObject):  
    while isinstance(tree,dict):  
        key = tree.keys()[0]
        #print key
        if tree[key].has_key(newObject[key]):
            tree = tree[key][newObject[key]]
        else:
            tree = "no"
    return tree  

def generateTree(treeFile,dataSetFile):
    file_tree = open(treeFile,'w')
    dataset,features = createDataSet(dataSetFile)  
    tree = treeGrowth(dataset,features)
    file_tree.write(str(tree))
    file_tree.close()
def getSessionIds():
    file_sessionIds = open('D:\Data\\feature\\yoochoose-test-sessionId.dat')
    sessionIds = []
    number = 0
    for sessionId in file_sessionIds:
        if number !=0:
            sessionIds.append(sessionId.strip())
        number+=1
    return sessionIds
def classifyTestData(treeFile,testDataFile,solutionFile):
    file_tree = open(treeFile)
    tree = {}
    for line in file_tree:
        tree = eval(line)
        break
    dataset,features = getTestDataSet(testDataFile)
    sessionIds = getSessionIds()
    testData = {}
    for feature in features:
        testData[feature] = 0
    file_solution = open(solutionFile,'w')
    totalYes = 0
    totalNo = 0
    number = 0
    rightNumber = 0
    for data in dataset:
        for i in range(len(features)):
            testData[features[i]] = data[i]
        value = predict(tree,testData)
        file_solution.write(str(sessionIds[number])+","+value+"\n")
        if value=="yes":
            rightNumber+=1
        number+=1
    print "buy rate: "+str(1.0*rightNumber/number)
    file_solution.close()
    

if __name__ == '__main__':
    #for i in range(17):
    #    generateTree('D:\Data\\solution\\tree-noWeekTime\\tree'+str(i)+'.dat',
    #                 'D:\Data\\feature\\balance-noWeekTime\yoochoose-feature-balence-'+str(i)+'.csv')
    for i in range(17):
        classifyTestData('D:\Data\\solution\\tree-noWeekTime\\tree'+str(i)+'.dat',
                         'D:\Data\\feature\\yoochoose-test-feature-noWeekTime.dat',
                         'D:\Data\\solution\\oneSolution-noWeekTime\\solution'+str(i)+'.dat')
    #print predict(tree,{'no surfacing':1,'flippers':1})  
    #print predict(tree,{'no surfacing':1,'flippers':0})  
    #print predict(tree,{'no surfacing':0,'flippers':1})  
    #print predict(tree,{'no surfacing':0,'flippers':0}) 
    
