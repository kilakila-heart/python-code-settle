#coding:cp936--*
import re
import time
#_BINARY_RE = '\\s*0\\s*,\\s*1\\s*'  ###pattern:

#with open('C:\Users\syh\Documents\misvm-master\example\musk1.data','r') as f:

def DelLastChar(string):
    '''删除字符串的最后一个字符,但要注意如果是文本中读入的
       最后一行字符串，则最后一个字符串是换行符，此外
       比较其与s[:-1]的效率有时间的话'''
    str_list=list(string)
    str_list.pop()
    return "".join(str_list)

def dataformat():
    i=0
    value=[]
    value_instance=[]
    d={}
    namefile_d_instance={} #从.names中读到的实例的字典
    namefile_d_bag={}      #从names中读到的包的字典
    d_feature={}
    with open('C:\\Users\\Administrator\\Documents\\misvm-car\\misvm-master\\example\\bagfeature.names','r') as f:
        for line in f:
            if(i==0):
                i+=1
                continue
            elif(i==1):
                mole_number=line.count(',')
                mole_name=line.split(',')
                print('分子个数为'+str(mole_number+1))
                for u in xrange(mole_number+1):
                    if u==0:
                        namefile_d_bag[''.join(mole_name[0]).split(':')[1].strip()]=u
                        continue
                    namefile_d_bag[mole_name[u].strip()]=u
                    if u==mole_number:
                       namefile_d_bag[''.join(mole_name[u]).split('.')[0].strip()]=u
            if line.startswith('molecule_name'):
                value=line.split(',')
                for j in range(len(value)):
                    d[value[j]]=j
                i+=1
            if(i==2):
                print('分子个数为'+str(len(value)))
                print('分子个数为'+str(len(d))) #验证包是否重复
                if(len(value)!=len(d)):
                    print(".names文件中包的数量有重复，attention")
                time.sleep(1)
                i+=1
                continue
            if line.startswith('conformation_name'):
                   value_instance=line.split(',')
                   example_number=line.count(',')
                   print('实例个数为'+str(len(value_instance)))
##                   print('memeda')
##                   print('happy')
                   for K in xrange(example_number+1):
                        if namefile_d_instance.has_key(value_instance[K]):#验证.names中实例是否重复
                            print('get .names中重复实例-----'+str(k))
                        elif K==0:
                            namefile_d_instance[''.join(value_instance[K]).split(':')[1].strip()]=K
                        elif K==example_number:
##                            print(''.join(value_instance[K]))
                      #待修改的代码      
                            namefile_d_instance[DelLastChar(''.join(value_instance[K]).strip())]=K
                            print(DelLastChar(''.join(value_instance[K]).strip()))
                            
                        else:
                            namefile_d_instance[value_instance[K].strip()]=K
                   print('实例个数为'+str(len(namefile_d_instance))) #验证实例是否重复
                      
            print('ssha')
    ##        print(i)
            if(i==3):
                example_number=line.split(',')
                print('实例个数为'+str(len(namefile_d_instance)))
                print('实例个数为'+str(len(example_number)))
                i+=1
            if(i==4):
                break
    line_number=0
    scale_a=0
    datafile_d_bag={}       #从.data中读到的包的字典
    datafile_d_instance={}  #从.data中读到的实例的字典
    instance_number_in_bag=1
    swap_instance_number_in_bag=0
    instance_in_bag={}
    P_N_label=0 #用标签的正确次数来匹配数据，观察测试集的标签是否准确
    pattern_nexample_car_extract="n\d(.*?),(.*?),(.*),0"
    ##pattern_nexample_car_extract="n(\d.*?,)(.*),-1"
    pattern_pexample_car_extract="p\d(.*?),(.*?),(.*),1"
    
    error_label_datafile_d_bag={}         #标签错误的包
    error_label_datafile_d_instance={}    #标签错误的包对应的实例行
    #with open('C:\Users\syh\Documents\misvm-master\example\musk1.data','r') as f:
    with open(r'C:\\Users\\Administrator\\Documents\\misvm-car\\misvm-master\\example\\bagfeature.data','r') as f:
        for line in f:
            bag_id=line.split(',')[0]
            instance_id=line.split(',')[1]  
            if  re.search(pattern_nexample_car_extract,line) is not None:
                P_N_label+=1
            elif  re.search(pattern_pexample_car_extract,line) is not None:
                P_N_label+=1
            else:
                error_label_datafile_d_bag[bag_id]=1
                error_label_datafile_d_instance[instance_id]=1
                 
            if datafile_d_instance.has_key(instance_id):
                print('get .names中重复实例-----'+str(instance_id))
            else:
                datafile_d_instance[instance_id.strip()]=line_number
               
            if datafile_d_bag.has_key(bag_id):         
                instance_number_in_bag+=1
                datafile_d_bag[bag_id]=instance_number_in_bag
    ##            instance_in_bag[instance_number_in_bag]=bag_id
            else:
                '''instance_in_bag这种设计方式有问题'''
##                if instance_in_bag.has_key(instance_number_in_bag):
##                    pass
##    ##            print('skip')
##                else:
##                    instance_in_bag[instance_number_in_bag]=bag_id
            
                instance_number_in_bag=1
                datafile_d_bag[bag_id]=instance_number_in_bag
                
            
            '''互相验证bag_id和instance_id是否相互存在于namefile和datafile中
               这里的报错要特别注意最后一个实例和第一个实例子，因为会遇到一些比较
               奇怪的数据'''
            if bag_id not in namefile_d_bag or instance_id not in namefile_d_instance:
                if bag_id not in namefile_d_bag:
                    print('there is some bag-error in namefile')
                    print('bag_id--'+bag_id)
                    print('----**----')
                if instance_id not in namefile_d_instance:
                    print('there is some instance-error in namefile')
                    print('instance_id--'+instance_id)
            line_number+=1
                #print(line.count(','))
            if line_number==1:
                scale_a=line.count(',')
            a=line.count(',')
            if a!=scale_a:
                print('----wrong-----')
            if len(namefile_d_instance)==line_number:
                a=line.count(',')
                print('特征数为'+str(a-2))
                print("attention!")
                #生成器表达式
                iter_error_datafile_d_bag=(ele_error_bag_label for ele_error_bag_label in error_label_datafile_d_bag)
                iter_error_datafile_d_instance=(ele_error_bag_label for ele_error_bag_label in error_label_datafile_d_instance)
                if P_N_label!=line_number:
                    for ele_err_bag in iter_error_datafile_d_bag:
                        for ele_err_instance in iter_error_datafile_d_instance:
                            print('包对应的标签有错误'+ele_err_bag+'---'+ele_err_instance)
                print('包中实例的个数为:')
##                key_iter=(key for key in instance_in_bag.keys())
##                for key_ele in key_iter:
##                    print key_ele
##                print(instance_in_bag)
                
    #return True
    return datafile_d_bag,datafile_d_instance,len(d),a-2


    '''
        datafile_d_bag          #从.data中读到的包的字典
        datafile_d_instance={}  #从.data中读到的实例的字典
                                #实例个数
        a-2                     #特征数
        以合适的形式打印出文本数据的特征
    '''
if __name__ == '__main__':
    dataformat()
















            
