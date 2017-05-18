def lucky_sum(a, b, c):
  sum=0
  if a!=13:
     sum=sum+a
     if b!=13:
         sum=sum+b
         if c!=13:
             sum=sum+c
 
  return sum

def lucky_sum_compare(a, b, c):
  sum=0
  if a!=13:
     sum+=a
     if b!=13:
         sum+=b
         if c!=13:
             sum+=c
  print sum
 
  return sum
if __name__ == '__main__':
    lucky_sum_compare(1, 2, 3)


