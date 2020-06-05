import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,99,484,74,98])

print(arr)

for a in np.nditer(arr):
    print(a)
