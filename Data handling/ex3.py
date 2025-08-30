import numpy as np
arr=np.array([1,2,3,4,5,6])
print(arr.reshape(2,3))
print(arr)
print(arr[1])
print(arr[-1])
print(arr[0])
print(arr[0:2])
print(arr[::2])#every second element lai herchha yesle
print(np.max(arr))
print(np.sum(arr))
print(np.mean(arr))
print(np.var(arr))
print(np.std(arr))
arr2d=np.array([[1,2,300],[4,5,6]])
print(arr2d.flatten())
print(np.max(arr2d))
print(np.min(arr2d,axis=1))
print(np.cov(arr2d))
print(np.corrcoef(arr2d))


