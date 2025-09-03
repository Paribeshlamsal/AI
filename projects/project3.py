import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("diabetes.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

X=df.drop('Outcome',axis=1)
y=df['Outcome']

print("Features \n",X.head())
print("Target \n",y.head())

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42)
print("X_train shape",X_train.shape)
print("X_test shape",X_test.shape)
print("y_train shape",y_train.shape)
print("y_test shape",y_test.shape)

model=LogisticRegression(max_iter=1000)
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test,y_pred)
print("Accuracy - ",accuracy)

new_patient = pd.DataFrame([[2, 120, 70, 25, 80, 28, 0.5, 33]], columns=X_train.columns)
prediction=model.predict(new_patient)
if prediction[0]==1:
    print("Yes diabetes")
else:
    print("No diabetes")

plt.hist(df['Glucose'], bins=20, color='skyblue', edgecolor='black')
plt.title("Glucose Distribution")
plt.xlabel("Glucose Level")
plt.ylabel("Frequency")
plt.show()

plt.scatter(df['Age'], df['BMI'], c=df['Outcome'], cmap='bwr', alpha=0.7)
plt.title("BMI vs Age (Colored by Diabetes Outcome)")
plt.xlabel("Age")
plt.ylabel("BMI")
plt.colorbar(label="Diabetes (0 = No, 1 = Yes)")
plt.show()

corr=df.corr()
plt.figure(figsize=(10,7))
sns.heatmap(corr,annot=True,cmap='coolwarm',linewidths=0.5)
plt.title("Correlation heatmap")
plt.show()

importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_[0]
}).sort_values(by='Coefficient', ascending=False)

print(importance)

import matplotlib.pyplot as plt

importance_sorted = importance.reindex(importance.Coefficient.abs().sort_values(ascending=False).index)

plt.figure(figsize=(10,6))
plt.barh(importance_sorted['Feature'], importance_sorted['Coefficient'], color='skyblue')
plt.xlabel("Coefficient Value")
plt.title("Feature Importance in Logistic Regression")
plt.gca().invert_yaxis() 
plt.show()
