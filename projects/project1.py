import numpy as np
np.random.seed(42)
data = np.array([
    [78, 85, 90, 1],
    [65, 70, 60, 0],
    [90, 95, 92, 1],
    [55, 60, 58, 0],
    [80, 82, 88, 1],
    [60, 65, 70, 0]
])
print("Dataset - \n",data)
features=data[:,:-1]
labels=data[:,-1]
print("Mean of features:",np.mean(features,axis=0))
print("Max of features:",np.max(features,axis=0))
print("Min of features:",np.min(features,axis=0))
positive_samples=data[data[:,-1]==1]
print("Rows with label \n",positive_samples)
train,test=np.array_split(data,[4])
print("Train set - \n",train)
print("Test set - \n",test)