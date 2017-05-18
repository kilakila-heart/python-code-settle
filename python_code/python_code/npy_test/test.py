#--*coding:utf-8 --*
import numpy as np
a = np.arange(0,12).reshape(3,4)
np.save('a.npy',a)
c=np.load('a.npy')
print c
