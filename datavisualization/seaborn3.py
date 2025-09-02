import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
tips=sns.load_dataset("tips")
corr=tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True,cmap='coolwarm',linewidths=0.5)
plt.title("Corelation heatmap of tips dataset")
plt.show()