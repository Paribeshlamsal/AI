import pandas as pd
data={
    'Name':['Ram','Shyam','Hari','Gita'],
    'Age':[20,None,20,15],
    'Score':[90,70,None,80]
}
df=pd.DataFrame(data)
print(df.isnull())
df_drop=df.dropna()
print(df_drop)
df_fill=df.fillna({'Age':df['Age'].mean(),'Score':df['Score'].mean()})
print(df_fill)
print(df.isnull().sum())