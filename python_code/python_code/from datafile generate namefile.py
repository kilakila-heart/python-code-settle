#coding:cp936--*
#!/usr/local env python

''' 16-3-24--14-46
    ������Щ������Ϊ�˸����Ѿ��õ���.data�ļ�����.names�ļ�
    �ڴ�֮ǰ������data format examine.pyĿ����Ϊ�˼�����ܵ�.name�ļ�����ȷ��
    ���ڿ��ǽ�������װ���������ģ�飡����'''
'''����õ���������molecule_name��conformation_name��һ�и�һ����ʱ����'''
    
import re
import time
from  data_format_examine import dataformat
symbol_str=raw_input("please input your names of your data feature: ")

line_index=1 
with open(symbol_str+'.names','w') as name_file:
    bag_id_set,instance_id_set,bag_len,feature_len=dataformat()
    bag_len=len(bag_id_set)
    instance_len=len(instance_id_set)
    while line_index < feature_len+4:
        if line_index==1:
            name_file.write('0,1.'+'\n')
            line_index+=1
        if line_index==2:
            name_file.write('molecule_name:')
            for bag_id in bag_id_set:               
                name_file.write(str(bag_id)+',')
            name_file.write('\n')
            line_index+=1
        if line_index==3:
            name_file.write('conformation_name:')
            for instance_id in instance_id_set:                
                name_file.write(str(instance_id)+',')
            name_file.write('\n')
            line_index+=1
        elif line_index > 3:
            name_file.write('f'+str(line_index-3)+': continuous scale=0.001.')
            line_index+=1
            name_file.write('\n')



    
