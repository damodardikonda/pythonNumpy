import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,99,484,74,98])

print(arr)

  #for a in np.nditer(arr):
    #   print(a)
#Transposing array anditerating
arra=np.arange(0,60,5)
print(arra)

arr2=arra.T# also arra.transpose()
print(arr2)


abc=np.array([1,2,3,4,5,6])
print(abc.flat[5])

arr3=np.array([[1,2,3],[6,7,8],[9,5,6]])
print(arr3)
c=arr3.flatten()
print(type(c))


b=arr3.ravel()
print(b)
print(type(b))

a1=np.array([[1,2,3,4],[5,6,7,8]])
a2=np.array([[9,10,11,12],[13,14,15,16]])
ar=np.concatenate((a1,a2),axis=0)#if axis is add by 1 theen it increase*2
print(ar)

cc=np.stack((a1,a2),1)
print(cc)

aaaa=np.arange(16).reshape(4,4)
print(np.split(aaaa,4))
print(np.hsplit(aaaa,4))
print(np.vsplit(aaaa,4))
