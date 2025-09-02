import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=np.random.randint(100,500,size=(5,5))
sns.heatmap(data,annot=True,cmap='coolwarm',linewidths=0.7)
plt.title("Random example using random")
plt.show()