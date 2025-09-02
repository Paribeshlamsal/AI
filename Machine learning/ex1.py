import pandas as pd
import matplotlib.pyplot as plt
data= {
    'Hours':[1,2,3,4,5],
    'Marks':[50,56,60,70,80]
}
df=pd.DataFrame(data)
print(df)
plt.scatter(df['Hours'],df['Marks'],color='blue')
plt.title("Hours vs Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

from sklearn.linear_model import LinearRegression
X=df[['Hours']]
y=df['Marks']
model=LinearRegression()
model.fit(X,y)
print("Slope (m)",model.coef_[0])
print("Intercept (c)",model.intercept_)

predicted_marks=model.predict([[6]])
print("Predicted marks for 6 hours",predicted_marks[0])

plt.scatter(X,y,color='blue')
plt.plot(X,model.predict(X),color='red')
plt.title("Hours vs Marks with regression line")
plt.xlabel("Hours studied")
plt.ylabel("Marks")
plt.grid(True)
plt.show()