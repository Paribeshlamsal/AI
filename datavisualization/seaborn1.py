import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
tips=sns.load_dataset("tips")
print(tips.head())
# sns.scatterplot(x='total_bill',y='tip',data=tips)
sns.barplot(x='day',y='total_bill',data=tips)
# sns.lineplot(x='total_bill',y='tip',data=tips)
# sns.histplot(tips["total_bill"],bins=20,kde=True)
# sns.boxplot(x='total_bill',y='tip',data=tips)
plt.show()