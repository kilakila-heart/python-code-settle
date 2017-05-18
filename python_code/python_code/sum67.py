#http://codingbat.com/prob/p108886
def sum67(nums):
    sum=0
    symbol_ignore=0
    for ele in nums:
        if symbol_ignore==0:
            if ele !=6:
                sum=sum+ele
            else:
                symbol_ignore=1
            continue
        elif ele==7:
             symbol_ignore=0
             continue
    return sum
#http://codingbat.com/prob/p167025
def sum13(nums):
    sum=0
    symbol_ignore=0
    for ele in nums:
        if symbol_ignore==0:
            if ele !=13:
                sum=sum+ele
            else:
                symbol_ignore=1
            
        else:
             symbol_ignore=0
    return sum
             
