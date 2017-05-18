#--*coding:utf-8 --*
'''简单用字典实现的词频统计
参考：http://zhidao.baidu.com/question/1510079567856937180.html
      http://www.cnblogs.com/BeginMan/p/3193081.html
      http://pmghong.blog.51cto.com/3221425/1349978
      http://qa.helplib.com/865296
'''
dic={}

for line in open('WordCount.txt','r'):
        array=[]
        line=line.strip()
        array=line.split()
        for j in array:
                if not dic.has_key(j):
                        dic[j]=0
                dic[j]+=1
sorted(dic.iteritems(), key=lambda d:d[0], reverse = False)
print(dic)
f=open('WordCount.txt','a')
f.write ('--------------------'+'\n')

for k,v in sorted(dic.iteritems(), key=lambda d:d[0], reverse = False):      
      f.write (k+'\t'+str(v)+'\n')
##    print(i+'\t'+str(value)+'\n')
f.close()
