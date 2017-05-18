#coding:cp936--*
import re
import time 
_BINARY_RE = '\\s*0\\s*,\\s*1\\s*'  ###pattern:
#with open('C:\Users\syh\Documents\misvm-master\example\musk1.data','r') as f:
with open('molename_test.txt','r') as f:
    for line in f:
            a=line.count(',')
            if a!=1491:
                    print('分子个数'+str(a+1))
##            print(line.count(','))
##            time.sleep(1)
##            break
            
            
