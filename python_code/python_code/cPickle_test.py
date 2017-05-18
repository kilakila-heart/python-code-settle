# -*- coding: utf-8 -*-
import cPickle as pickle  
import time
import os
'''用pickle保持持久化对象
    但似乎很难去保存对象'''
def cPickle_test(debug_symbol): #变量系列化  
    t1 = ('this is a string', 42, [1, 2, 3], None)
    p1 = pickle.dumps(t1)
    t2 = pickle.loads(p1)
   
    if os.path.isfile('dump.txt'):
        f = open('dump.txt', 'rb')
        d = pickle.load(f)    
        f.close()
        debug_print(debug_symbol,d)
    else:     
        f = open('dump.txt', 'wb')
        pickle.dump(t1, f)
        f.close()


def debug_print(debug_symbol,string):
    if debug_symbol:
        print(string)
    else:
        pass
    
if __name__ == '__main__':
    debug_symbol=True
    cPickle_test(debug_symbol)
















            
