#--coding:utf-8--*
#这段代码是为了想起以前的将字典写入文件的方法
def generateOneClickBuysRate(buyInfoFile,clicksFile,oneClickBuysRateFileOut):#求一次点击的购买率
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
                if eachNumber==1:#只点击了一次
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

if __name__=='__main__':
    generateOneClickBuysRate('yoochoose-buys-info.dat','yoochoose-clicks.dat','yoochoose-buysRate-oneClick.dat')
