#--*coding:utf-8 --*
#!/usr/bin/env python

import os
import numpy as np
C_para = np.array(np.arange(1.0,0,-0.1),np.float)
threshold = np.array(np.arange(-1,1,0.1))
print C_para
print('-----分割线1-----------')
for ele in C_para:
    print ele
print('-----分割线2-----------')
for i in xrange(len(C_para)):
    print C_para[i]
print('-----分割线3-----------')
'''循环使用'''
for x, y  in zip(C_para,threshold):
    print x,y
print('-----分割线4-----------')
    
