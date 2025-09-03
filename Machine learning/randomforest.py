import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
df=pd.read_csv("diabetes.csv")
print(df.head())

X=df.drop('Outcome',axis=1)
y=df['Outcome']

print("Features - \n",X.head())
print("Target - \n",y.head())

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.25,random_state=42
)
print("Training Features",X_train.head())
print("Testing Features",X_test.head())

rf_model=RandomForestClassifier(n_estimators=100,random_state=42)
rf_model.fit(X_train,y_train)

y_pred=rf_model.predict(X_test)
print("Predictions - ",y_pred)

accuracy=accuracy_score(y_test,y_pred)
print("Accuracy is ",accuracy)

feature=pd.DataFrame({
    'Feature':X.columns,
    'Importance':rf_model.feature_importances_
}).sort_values(by='Importance',ascending=False)

print('Feature importance \n',feature)

new_data = pd.DataFrame([[2, 120, 70, 20, 79, 25.0, 0.5, 30]],columns=X_train.columns)
new_prediction=rf_model.predict(new_data)
if new_prediction[0]==1:
    print("Random tree prediction - Yes diabetes")
else:
    print("Random tree prediction - No diabetes")

plt.figure(figsize=(20,10))
plt.barh(feature['Feature'],feature['Importance'],color='red')
plt.title("Feature importance")
plt.xlabel("Importance")
plt.show()