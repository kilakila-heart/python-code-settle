#coding:cp936 --*
import os.path
import pprint
import os
import os.path
'''
    os.walk���ĳ���Ǳ���һ��Ŀ¼���õ�ģ�飬������һ������3��Ԫ�ص�Ԫ��:dirpath,dirnames,filenames.
    dirpath����string�ַ�����ʽ���ظ�Ŀ¼�����еľ���·����
    dirnames�����б�list��ʽ����ÿһ������·���µ��ļ������֣�
    filesnames�����б�list��ʽ���ظ�·���������ļ����֡�
'''
filename="E://paper"
for root, dirs, files in os.walk(filename):
    #print dirs
    for name in files:
        print(root) #----��Ŀ¼�����еľ���·����
        print name
