import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data = {
    'Age': [22, 25, 30, 35, 40, 45, 50, 55],
    'Glucose': [85, 89, 92, 120, 130, 150, 160, 170],
    'BMI': [18, 20, 21, 25, 28, 30, 32, 34],
    'Diabetes': [0, 0, 0, 1, 1, 1, 1, 1] 
}

df = pd.DataFrame(data)
print(df)

X=df[['Age','Glucose','BMI']]
y=df['Diabetes']

print("Features \n",X)
print("Target \n",y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=42)
print("Training Features (X_train):")
print(X_train)

print("\nTesting Features (X_test):")
print(X_test)

print("\nTraining Target (y_train):")
print(y_train)

print("\nTesting Target (y_test):")
print(y_test)

model=LogisticRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
print(y_pred)

accuracy=accuracy_score(y_test,y_pred)
print("Accuracy - ",accuracy)

new_data=pd.DataFrame([[33,115,20]],columns=['Age','Glucose','BMI'])
prediction=model.predict(new_data)
if prediction[0]==1:
    print("Diabetes - yes")
else:
    print("Diabetes - no")