import pandas as pd
product=[
    ['Laptop',20000,5],
    ['Phone',10000,3],
    ['Tablet',1000,6],
    ['Monitor',15000,4]

]
df=pd.DataFrame(product,columns=['Device','Price','Quantity'])
print(df)
print(df['Price'])
print(df.loc[1])
print(df['Quantity'])
print(df.loc[3])
high=df[(df['Price']>5000) & (df['Quantity']>3)]
high1=df[df['Price']>5000][['Device']]
print(high)
print(high1)