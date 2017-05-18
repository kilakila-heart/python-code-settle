#coding:cp936--*
'''3-25用于准确度的单元测试
'''
TRUE_labels_number=0.0
instance_len_labels_predictions=0
sign = lambda x: 1 if x > 0 else -1 if x < 0 else 0
with open(r'C:\Users\Administrator\Documents\misvm-car\misvm-master\Initial results\1.txt','r') as f:
    
    for line in f:
            a=sign(float(line.split(',')[1].strip('\n')))
            if a>0:
                TRUE_labels_number+=1
            instance_len_labels_predictions+=1
    accuracy=TRUE_labels_number/instance_len_labels_predictions
    print(accuracy)
    print '%.1f%%' % (100 * accuracy)         
            
