#coding:cp936 --*
import re
import time
i=0
d={}
pattern_test="<CLASS,\ CLASS,\ None>\), \['(.*?),(.*?),"
with open('C:\\0.asv','r') as file:
    for line in file:
        if  re.search(pattern_test,line) is not None:
            searchObj=re.search(pattern_test,line)
            if searchObj:
                d[str(i)]=searchObj.group(1)+','+searchObj.group(2)
                value=d.values()
    print(value)
        
        
