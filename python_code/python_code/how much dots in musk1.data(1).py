#coding:cp936--*
import re
import time 
_BINARY_RE = '\\s*0\\s*,\\s*1\\s*'  ###pattern:
##with open('C:\Users\syh\Documents\misvm-master\example\musk1.data','r') as f:
with open(r'C:\Users\Administrator\Documents\misvm-master\example\bagfeature.data','r') as f:
    for line in f:
            #print(line.count(','))
            a=line.count(',')
            if a!=872:
                    print("attention!")
                    print(a)
                    time.sleep(20)
            
with open(r'test.txt','r') as f_test:
     for line in f_test:
             b=line.count(',')
             print b
            
