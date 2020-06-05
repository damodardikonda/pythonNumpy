#annonymous function
#import sys
import numpy as np
#f=lambda a:a*a

#print(f(5))


#g= lambda a,b:a+b
#print(g(10,20))


#h_letter=[letter for letter in 'human']
#print(h_letter)



#if sys.version_info.major == 3:
#    print('Python3')
#else:
#    print('Python2')


#arr=np.array([[1,2,3],[4,5,6],[6,7,8],[9,4,6]])

#print("the type of array is"+type(arr))
#print("the shape of array is"+str(arr.shape))
#print("dimesion"+arr.ndim)
#print("size is "+arr.size)
#print("type of the element"+arr.dtype)

#printing siple one dimesion array
arr=np.array([1,2,3])
print(arr)

a=np.array([[1,2,3],[4,5,6],[8,7,9]])

print(a)

#shows type of array
print(type(a))

#shape of array
print(a.shape)

#"dimesion" of array
print(a.ndim)

#print("type of the element"+
print(a.dtype)
b= np.array([1, 2, 3], dtype = complex)
print(b)

dt=np.dtype('i8')
print(dt)
ar=np.array([12,3,4,5])
print(np.dtype([('ar',np.float)]))

student=np.dtype([('name','S20'),("rsoll",'i4'),('mark','f4')])
s=np.array([("xyz",20,30),("zab",30,40)], dtype=student)
print(s)

arrays=np.array([1,2,3,4,5,6,7,8,9,0,12,14,22,33,56,76,])
p=arrays.reshape(4,4)
print(p)


arrays=np.array([1,2,3,4,5,6,7,8,9,0,12,14,22,33,56,76,23,43])
d=arrays.reshape(2,3,3)
print(d)
print(d.flags)

#empty in numby

#nn=np.empty([3,4],dtype=int)
#print(nn)

#ab=np.array([1,2,3,4,5,6,7,8,9,0,12,14,22,33,56,76,23,43])
#print(ac)

#zeros
print(np.zeros(5))
print(np.zeros([2,2], dtype=int))

#fromiter() is used to create ndarray from object

aaa =range(5)
a1=iter(aaa)
print(a1)
#ones
print(np.ones(8))




#frombuffer work as buffer
#str="heeeeeeeeeeellllllllllllloooooooooooooooooooo wwwwwwwwwwwoooooooooooooorrrrrrrrrrrrllddddddddddddddddddddddddd"
#n=np.frombuffer(str,dtype='S1')
