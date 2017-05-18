#coding:cp936
#!/usr/bin env python

import re
import time
import os
from pprint import pprint

pattern_test_car_instance="(.*?),(.*?),\?.$"
test_instance_id={}
test_instance_array={}
line_number=0
with open(r'testfeature.txt','r') as test_feature_f:
    for line in test_feature_f:
        if re.match(pattern_test_car_instance,line) is not None:
            searchObj=re.match(pattern_test_car_instance,line)
            if searchObj:
                    test_instance_id[str(line_number)]='Intance-id-'+''.join(searchObj.group(1)) #实例的id
##                    print(''.join(searchObj.group(2)))
                    test_instance_array[str(line_number)]=searchObj.group(2)
        
        line_number+=1
        pprint(test_instance_id)
        pprint(test_instance_array)
        time.sleep(5)
            
        
