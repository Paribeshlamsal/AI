import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = {
    "Hours_Studied": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Hours_Sleep": [8, 7, 6, 7, 5, 6, 7, 6, 5, 7],
    "Hours_Revision": [0, 1, 1, 2, 2, 3, 3, 4, 4, 5],
    "Marks": [50, 52, 55, 60, 63, 65, 70, 74, 78, 80]
}
df=pd.DataFrame(data)
print(df)

# sns.pairplot(df)
# plt.show()

# sns.heatmap(df.corr(),annot=True,cmap='coolwarm')
# plt.show()

X=df[['Hours_Studied','Hours_Sleep','Hours_Revision']]
y=df['Marks']

model = LinearRegression()
model.fit(X,y)
print("Slope(m)",model.coef_[0])
print("Intercept (c)",model.intercept_)

predicted_marks=model.predict([[11,4,2]])
print("Predicted Marks = ",predicted_marks[0])

plt.scatter(y,model.predict(X),color='green')
plt.title("Data Visualization")
plt.xlabel("Actual Marks")
plt.ylabel("Predicted Marks")
plt.grid(True)
plt.show()