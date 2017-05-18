# ---*coding:cp936 --*
import string
import math
####密切注意缩进#######
#编译通过可能还是有语法错误，要加以注意
def percent_Monthlen_items():
#判别长项目在购买量上占项目总的购买量的比例，从而探查项目的购买时长对项目的销售的影响
    s={} 
    buyMonthlen = getDicFromFile('D:\Data\yoochoose-buyMonthLen.dat')
    for N in range(1,7): #月份长设置  
        file_name='D:\Data\yoochoose-buys-percent_Monthlen_items'+str(N)+'.dat'
        file_percent_Monthlen_items=open(file_name,'w')
        file
        for item in  buyMonthlen:
            if buyMonthlen[item]>=N:
                s[item]=1                  #len(monthlen) ###buy中总的项目数
        print "N="+str(N)+"\t"+str(len(s))+"\t"+str(len(buyMonthlen))+"\t"+str(1.0*len(s)/len(buyMonthlen))
        file_percent_Monthlen_items.write(str(s))
        s={}
    file_percent_Monthlen_items.close()


    
##购买中月份长的分布
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
    file_object_w.write("项目月份长"+":\t"+"出现次数"+"\n")
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
