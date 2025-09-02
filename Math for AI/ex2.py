import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
print(tips.head())
mean_tip=tips['tip'].mean()
print("Mean for tip is",mean_tip)
median_tip=tips['tip'].median()
print("Median for tip is",median_tip)
mode_tip=tips['tip'].mode()[0]
print("Mode for tip is",mode_tip)

range_tip=tips['tip'].max()-tips['tip'].min()
var_tip=tips['tip'].var()
std_tip=tips['tip'].std()
print("Range for tip is",range_tip)
print("Variance for tip is",var_tip)
print("Standard deviation for tip is",std_tip)



correlation=tips[["total_bill","tip"]].corr()
print("The correlation is \n",correlation)
covariance=tips[["total_bill","tip"]].cov()
print("The covariance is \n",covariance)
plt.hist(tips['tip'],bins=20,color='red',edgecolor='black')
plt.title("Distribution of tips")
plt.xlabel("Tip amount")
plt.ylabel("Frequency")
plt.show()

sns.heatmap(correlation,annot=True,cmap="coolwarm")
plt.show()