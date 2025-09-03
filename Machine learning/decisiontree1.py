import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df=pd.read_csv("diabetes.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
 
X=df.drop('Outcome',axis=1)
y=df['Outcome']

print("Features \n",X.head())
print("Targer \n",y.head())

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.25,random_state=42
)

print("Training features \n",X_train.head())
print("Testing features \n",X_test.head())

dt_model=DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train,y_train)
y_pred=dt_model.predict(X_test)
print("Prediction on test data",y_pred)

accuracy=accuracy_score(y_test,y_pred)
print("Accuracy is - ",accuracy)

feature_importance=pd.DataFrame({
    'Feature':X.columns,
    'Importance':dt_model.feature_importances_
}).sort_values(by='Importance',ascending=False)
print("Feature importance - \n",feature_importance)

new_data = pd.DataFrame([[2, 120, 70, 20, 79, 25.0, 0.5, 30]],columns=X_train.columns)
pred_new=dt_model.predict(new_data)
if pred_new[0]==1:
    print("Decision tree prediction - Yes diabetes")
else:
        print("Decision tree prediction - No diabetes")


# plt.figure(figsize=(20,10))
# plot_tree(
#     dt_model,
#     feature_names=X.columns,
#     class_names=['Diabetes','No Diabetes'],
#     filled=True,
#     rounded=True,
#     fontsize=12
# )
# plt.show()