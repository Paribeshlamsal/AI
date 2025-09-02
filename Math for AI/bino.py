import numpy as np
import matplotlib.pyplot as plt
binom_data=np.random.binomial(n=10,p=0.5,size=1000)
plt.hist(binom_data,bins=10,edgecolor='black',color='red')
plt.title("Binomial distribution example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()