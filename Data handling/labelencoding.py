import pandas as pd
from sklearn.preprocessing import LabelEncoder
df=pd.DataFrame({
    'Size': ['Small', 'Medium', 'Large', 'Medium', 'Small']
})
print(df)
le=LabelEncoder()
df['Size_label']=le.fit_transform(df['Size'])
print(df)