import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import seaborn as sns
data = {
    "Glucose": [85, 90, 78, 120, 110, 95, 130, 100],
    "BMI": [18, 20, 22, 30, 28, 25, 32, 27],
    "Age": [22, 25, 28, 35, 32, 30, 40, 36],
    "Diabetes": [0, 0, 0, 1, 1, 0, 1, 1]  # 0 = No, 1 = Yes
}

df = pd.DataFrame(data)
print(df)

sns.pairplot(df, hue="Diabetes")
plt.show()

X=df[['Glucose','BMI','Age']]
y=df['Diabetes']

model=LogisticRegression()
model.fit(X,y)
print("Slope - ",model.coef_[0])
print("Intercept - ",model.intercept_)

prediction=model.predict([[70,29,33]])
if prediction[0]==1:
    print("Predcition - Diabetes")
else:
    print("Prediction - No Diabetes")

from sklearn.metrics import accuracy_score
predictions=model.predict(X)
accuracy=accuracy_score(y,predictions)
print("Training accuracy",accuracy)
