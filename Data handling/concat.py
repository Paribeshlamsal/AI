import pandas as pd
data1={
    'Name':['Ram','Shyam','Hari'],
    'Age':[15,16,14]
}
data2={
    'Name':['Gita','Sita','Rita'],
    'Age':[18,15,19]
}
df=pd.DataFrame(data1)
df1=pd.DataFrame(data2)
result=pd.concat([df,df1])
print(result)
result1=pd.concat([df,df1],axis=1)
print(result1)
