#--*coding:cp936 --*
import string
import sys
def kkd(n,m):
    x={};y={};i=0;j=0
  
    if(n==m==0):
        sys.exit(1)
    for i in range(n):#这里改变了i
        x[i]=input("the number of n")
    for j in range(m):#这里改变了j，注意！！！！
        y[j]=input("the number of m")
    dragon_head=x.values()
    knight_power=y.values()
    knight_power.sort()
    dragon_head.sort()
    sum=0;i=0;j=0
    #print knight_power
    while True:
        if i <len(dragon_head):      
                if knight_power[j]<dragon_head[i]:
                    j+=1
                else:
                    sum+=knight_power[j]
                    i+=1
                    j+=1
                    
                if i==len(dragon_head):
                       print  sum
                       break
                if j==len(knight_power):
                    print "Lowwater is doomed!"
                    break
if __name__=='__main__':
      while True:
          n,m=input("please input n"),input("please input m")
          if (n==0 and m==0):
              break
          else:kkd(n,m)
                
        
    
