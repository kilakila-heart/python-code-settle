# --*coding:cp936 --*
import math
import string
def item_clickbutNOBUY():
    file_object=open('D:\Data\yoochoose-clicks.dat')
    file_itemClickNotBuy=open("D:\Data\yoochoose-Item-clickNotBuy.dat",'w')
    file_Just_itemClickNotBuy=open("D:\Data\yoochoose-Item-cNB_just_Item.dat",'w')
    itemPrice=getDicFromFile('D:\Data\yoochoose-buys-itemPrice.dat')
    i=0
    j=0
    s={}
    for line in file_object:
        i+=1
        if i%100000==0:
            print i
        data=line.split(",")
        itemId=data[2]
        if itemPrice.has_key(itemId):
            continue
        file_itemClickNotBuy.write(data[0]+"\t"+itemId+"\n")
        s[itemId]=1
        j+=1   #写入的次数
    file_Just_itemClickNotBuy.write(str(s))
    print j          #1348034
    print len(s)     #32790  有32790个项目在过去被点击而一次都没有购买
    
    file_itemClickNotBuy.close()
    
    
def getDicFromFile(fileName):#项目及其次数的字典
    file1 = open(fileName)
    dic = {}       
    for line in file1:
       dic=eval(line)  #注意这里的语法格式
    return dic
item_clickbutNOBUY()
