#-coding:cp936--*
import re
j=0
f = open(r'C:\Users\Administrator\Documents\misvm-master\example\musk1.data','r')
for i in f.readlines()[0:1] :
        print(i.count(','))
