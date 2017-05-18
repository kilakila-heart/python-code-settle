#--*coding:cp936 --*
import string
import sys
x={};y={};i=0;j=0
n,m=input("please input n"),input("please input m")
if(n==m):
    sys.exit(1)
for i in range(n):
    x[i]=input("the number of n")
for j in range(m):
    y[j]=input("the number of m")
dragon_head=x.values()
knight_power=y.values()
knight_power.sort()
dragon_head.sort()
print knight_power
print dragon_head
k=0
s=0
w=0
dragon_len=len(dragon_head)
#print knight_power
for ele in dragon_head:   
        print ele
        if knight_power[k]<ele:
            k+=1
        else:
            s+=knight_power.pop(k)
            print s
            dragon_head.pop(0)
            print "dragon_head"+str(dragon_head[:])
            w+=1
            
            if w==dragon_len:
               print  s
            if len(knight_power)==0:
                print "Lowwater is doomed!"
        continue
        
        
    
