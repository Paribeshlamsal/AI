import pandas as pd
data = {
    'Name':['Ram','Shyam','Sita','Hari'],
    'Score':[50,60,70,60],
    'Age':[15,12,17,11]
}
df=pd.DataFrame(data)
print(df)
data1=[
    ['Ram',70,11],
    ['Shyam',50,15],
    ['Hari',76,12]
]
df1=pd.DataFrame(data1,columns=['Name','Score','Age'])
print(df1)
print(df['Name'])
print(df.iloc[0,2])