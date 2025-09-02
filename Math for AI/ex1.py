import numpy as np
from scipy import stats
data=[1,2,3,4,5]
mean_m=np.mean(data)
median_m=np.median(data)
mode_m=stats.mode(data)
print(mean_m)
print(median_m)
print(mode_m[0])
range_m=max(data)-min(data)
vari=np.var(data)
stdv=np.std(data)
print(range_m)
print(vari)
print(stdv)