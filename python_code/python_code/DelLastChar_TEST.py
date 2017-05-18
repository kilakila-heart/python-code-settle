#coding:cp936--*
import time

def DelLastChar(string):
    '''删除字符串的最后一个字符,
       比较其与s[:-1]的效率有时间的话'''

    str_list=list(string)
    str_list.pop()
    return "".join(str_list)

string_test="3_8_positive_5M_0_5M_9_1.000.jpg."
print(DelLastChar(''.join(string_test)).strip())
