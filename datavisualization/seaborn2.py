import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
sns.pairplot(tips,hue="smoker",diag_kind="kde")
plt.show()