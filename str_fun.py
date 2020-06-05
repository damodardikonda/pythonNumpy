import numpy as np

arr1=np.array(['hi','hello'])
arr2=np.array(['damodar','dikonda'])
print(np.char.add(arr1,arr2))

#a=np.array([1,2,3,4])
#b=np.array([5,6,7,8])
#print(np.int.add(a,b))

print(np.char.multiply('hello ',3))

print(np.char.center(arr1,50,fillchar='*'))

print(np.char.capitalize('hello world'))

print(np.char.join(':','abcddd'))

print(np.char.replace('he was a good boy','was','is'))


#6	lower()
#7	upper()
#8	split()
#9	splitlines()
#10	strip(

#13	decode()
#14	encode()
