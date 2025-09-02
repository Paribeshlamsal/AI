import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [50, 52, 55, 60, 63, 65, 70, 74, 78, 80]
}
df=pd.DataFrame(data)
print(df)
# plt.scatter(df['Hours'],df['Marks'],color='red')
# plt.title("Big data Hours vs Marks")
# plt.xlabel("Hours")
# plt.ylabel("Marks")
# plt.grid(True)
# plt.show()

X=df[['Hours']]
y=df['Marks']

model=LinearRegression()
model.fit(X,y)
print("Slope (m)",model.coef_[0])
print("Intercept (c)",model.intercept_)

predicted_marks=model.predict([[11]])
print("Predicted marks for 11 is ",predicted_marks[0])

plt.scatter(X,y,color='red')
plt.plot(X,model.predict(X),color='green',linewidth=2)
plt.title("Big dataset Hours vs Marks")
plt.xlabel("Hours studied")
plt.ylabel("Marks")
plt.grid(True)
plt.show()
