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
        j+=1   #д��Ĵ���
    file_Just_itemClickNotBuy.write(str(s))
    print j          #1348034
    print len(s)     #32790  ��32790����Ŀ�ڹ�ȥ�������һ�ζ�û�й���
    
    file_itemClickNotBuy.close()
    
    
def getDicFromFile(fileName):#��Ŀ����������ֵ�
    file1 = open(fileName)
    dic = {}       
    for line in file1:
       dic=eval(line)  #ע��������﷨��ʽ
    return dic
item_clickbutNOBUY()
