import numpy.matlib
import numpy as np

print(np.matlib.empty((2,2)))
#print(np.matlib.zeros(2,2))
print(np.matlib.eye(n = 3, M = 4, k = 2, dtype = float))


print(np.matlib.identity(5, dtype="float"))


print(np.matlib.rand(2,2))

i=np.matrix('1,2;3,4;5,6,')
print(i)

#dot product

a=np.array([[1,2],[3,4]])
b=np.array([[98,45],[35,56]])
print(np.dot(a,b))

a=np.array([[1,2],[3,4]])
b=np.array([[98,45],[35,56]])
print(np.vdot(a,b))

print(np.inner(a,b))

print(np.matmul(a,b))
