# ---*coding:cp936 --*
import string
import math
####����ע������#######
#����ͨ�����ܻ������﷨����Ҫ����ע��
def percent_Monthlen_items():
#�б���Ŀ�ڹ�������ռ��Ŀ�ܵĹ������ı������Ӷ�̽����Ŀ�Ĺ���ʱ������Ŀ�����۵�Ӱ��
    s={} 
    buyMonthlen = getDicFromFile('D:\Data\yoochoose-buyMonthLen.dat')
    for N in range(1,7): #�·ݳ�����  
        file_name='D:\Data\yoochoose-buys-percent_Monthlen_items'+str(N)+'.dat'
        file_percent_Monthlen_items=open(file_name,'w')
        file
        for item in  buyMonthlen:
            if buyMonthlen[item]>=N:
                s[item]=1                  #len(monthlen) ###buy���ܵ���Ŀ��
        print "N="+str(N)+"\t"+str(len(s))+"\t"+str(len(buyMonthlen))+"\t"+str(1.0*len(s)/len(buyMonthlen))
        file_percent_Monthlen_items.write(str(s))
        s={}
    file_percent_Monthlen_items.close()


    
##�������·ݳ��ķֲ�
def buy_month_len():
    filename='D:\Data\yoochoose-buy-Monthlen-Item_distribution.dat'   
    file_object_w=open(filename,'w')
    buyMonthlen = getDicFromFile('D:\Data\yoochoose-buyMonthLen.dat')
    file_object3 = open('D:\Data\yoochoose-buys.dat')
    s={}
    number=0
    for line in file_object3:
        number+=1
        if number%10000==0:
            print number
        data=line.split(",")
        item =data[2]
        if buyMonthlen.has_key(item):
           if s.has_key(buyMonthlen[item]):
               s[buyMonthlen[item]]+=1
           else:
               s[buyMonthlen[item]]=1
    s = sorted(s.iteritems(),key=lambda s:s[0],reverse=False)
    file_object_w.write("��Ŀ�·ݳ�"+":\t"+"���ִ���"+"\n")
    for s_ in s:
        file_object_w.write(str(s_[0])+":\t"+str(s_[1])+"\n")
        print str(s_[0])+":\t"+str(s_[1])+"\n"
        
def getDicFromFile(fileName):
    file1 = open(fileName)
    dic = {}
    for line in file1:
        dic = eval(line)
        return dic
#percent_Monthlen_items()
#buy_month_len()
'''
percent_Monthlen_items() output:
N=1	19949	19949	1.0
N=2	13160	19949	0.659682189583
N=3	9420	19949	0.472204120507
N=4	6552	19949	0.328437515665
N=5	4354	19949	0.218256554213
N=6	2427	19949	0.121660233596
buy_month_len() output:
1:	97061
5:	150215
4:	166028
3:	189805
2:	232550
6:	315094
'''
