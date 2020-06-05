import numpy as np;

abc=np.arange(5)
print(abc)

num=np.arange(0,20,2)
print(num)

n=np.arange(0,1000,10,dtype=float)
print(n)

x=np.linspace(10,50,5,endpoint = True) # here 2 means divide no in 2 variable 10,50. if 3=10,30,50
print(x)

bc=np.linspace(10,50,5,retstep=0.5)
print(bc)

#logspace
ss=np.logspace(1,100,base=2)
print(ss)

#slicing array of item

a = np.arange(10)
s = slice(2,7,2)
print(a[s])

c=np.arange(10)
dd=c[2:8:2]
print(dd)


first=np.array([[1,2,3],[4,5,6],[7,8,9]])
second=first[[0,1,2],[1,0,2]]
print(second)

n=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x)
z=n[n>5]#op=6,7,8,9
print(z)
#row=np.array([[0,0],[2,2]])
#val=np.array([[1,3],[0,2]])
#v=x[row,val]
#print(v)


ad=np.array([[1,np.nan],[2,34,np.nan]])
print(ad[~np.isnan(ad)])#1,2,34
#as like thei iscomplex()which returns complexn
