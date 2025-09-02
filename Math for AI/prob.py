import numpy as np
import matplotlib.pyplot as plt
normal_data=np.random.normal(loc=50,scale=10,size=1000)
plt.hist(normal_data,bins=30,color='skyblue',edgecolor='black')
plt.title("Normal distribution example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()