import numpy as np

arr=np.array([0,20,45,60,90])

sine=np.sin(arr*np.pi/180)
print(sine)
print('\n')

cosin=np.cos(arr*np.pi/180)
print(cosin)

tane=np.tan(arr*np.pi/180)
print(tane)


a=np.array([1,0.6,5,7,8.9,9.4])
s=np.round(a)
print(s)
mins=np.round(a,decimals=-1)
plus=np.round(a,decimals=1)
print(mins)
print(plus)

#numpy.floor()
#This function returns the largest integer not greater than the input parameter i<=x

print(np.floor(a))


#numpy.ceil()
#The ceil() function returns the ceiling of an input value, i.e. the ceil of the scalar x is the smallest integer i, such that i >= x.

print(np.ceil(a))


dddd=np.array([1,2,3,4,5,7,6,70,475,743])

recip=np.reciprocal(dddd)
print(recip)

powers=np.power(dddd,2)
print(powers)

ccc=np.array([3,5,6,7,2,9,2,8,5,67])
mode=np.mod(dddd,ccc)
print(mode)


remainder=np.mod(dddd,ccc)
print(remainder)


accesss = np.array([[3,7,5],[8,4,3],[2,4,9]])


print(a)


# 1 for row
print(np.amin(a,1));

 # o for olumn
print(np.amin(a,0))

#bydfaut is 1 i.e row
print(np.amax(a))



print(np.amax(a, axis = 0))
