import numpy as np 
l = [[1,2,3,5,45,90],[10,12,90,34,55,66]]
arr = np.array(l)  # .array Convert into array
print(arr)
a = np.arange(1,3,dtype=np.int32)  # arange works same as range in list
print(a)
a = np.linspace(2,3,6)   # linspace generate number between given numbers
print(a)
print(arr[1,2])
print(arr[1][4])  # print same as 2-d array 

brr= arr.reshape(3,4)  # reshape will change row and columnn number
print(brr)

a2 = np.ones([3,3])   # all element value will be 1 in 2-d array
print(a2)

a3 = np.empty([3,3] ,order='F')
print(a3)

a4 = np.zeros([3,3]) # make array with all element as 0
print(a4)

print(brr[0:2 , 1:3])  # 2-d array slicing 