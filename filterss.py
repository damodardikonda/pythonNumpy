#filter returns a sequence

#without using lambda
from functools import reduce

def ev(n):
  if n%2==0:
      return n;
num=[1,2,3,4,5,6,7,8,9,10]

res=list(filter(ev,num))
print(res)


#using lambda

nums=list(filter(lambda n:n%2==0,num))
print(nums)
# adding adding 2 in even numbers with using map.we can also used an function insted of lambda
d=list(map(lambda n:n+2,nums))
print(d)
# adding whole numbers with using reduce.we can also used an function insted of lambda
red=reduce(lambda a,b:a+b,d)
print(red)
