#coding:utf-8
#!/usr/bin/env python
import numpy as np
import time
import re
import os
from sklearn.externals import joblib
import json
pattern_matrix_generate="np.matrix(.*)\)$"
_x_dict={}
x= np.matrix([[1, 2], [3, 4]])
middle_X=str(x)
middle_x_re=middle_X.replace('\n',',')
axis_H=middle_X.count('\n')
matrix_middle_x=np.matrix(middle_x_re)
matrix_middle_x_final=matrix_middle_x.reshape((axis_H+1,-1))
if  re.search(pattern_matrix_generate,middle_X) is not None:
     searchObj=re.search(pattern_matrix_generate,middle_X)
     _x_dict[1]=searchObj.group(1)
     B=np.matrix[_x_dict[1]]
     print(B)
