import numpy as np
arr=np.array([1,2,3,4,5])
print(arr)
greaterthan3=arr[arr>3]
print(greaterthan3)
arr[arr<3]=0
print(arr)
indices=[0,1,4]
ab=arr[indices]
print(ab)
