#--*coding:utf-8 --*
import random 
list = [88,89,90,91, 92,93,94,95,96,97, 98,99,100]  
slice = random.sample(list, 5)  #从list中随机获取5个元素，作为一个片断返回  
print slice  
#print list #原有序列并没有改变
