#coding:cp936--*
#!/usr/bin/env python
import os
import time

i=0
j=input("please enter your number:")
if os.path.isdir('file_write_test'):
    pass
else:
    os.makedirs('file_write_test')
with open('file_write_test//test.txt','w') as f:
    for i in range(j):
        f.write(str(i)+"\n")
    
    
