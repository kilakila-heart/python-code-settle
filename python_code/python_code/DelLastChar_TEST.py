#coding:cp936--*
import time

def DelLastChar(string):
    '''ɾ���ַ��������һ���ַ�,
       �Ƚ�����s[:-1]��Ч����ʱ��Ļ�'''

    str_list=list(string)
    str_list.pop()
    return "".join(str_list)

string_test="3_8_positive_5M_0_5M_9_1.000.jpg."
print(DelLastChar(''.join(string_test)).strip())
