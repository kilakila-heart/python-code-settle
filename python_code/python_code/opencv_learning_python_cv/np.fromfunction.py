#--*coding:utf-8
import numpy as np
from pprint import pprint 
def func(i):
    print 'call!'
    return i%4
print np.fromfunction(func, (10,))
