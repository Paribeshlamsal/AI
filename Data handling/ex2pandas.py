import pandas as pd
product=[
    ['Laptop',20000,5],
    ['Phone',10000,7],
    ['Keyboard',1000,4],
    ['Tablet',11000,6]
]
df=pd.DataFrame(product,columns=['Devices','Price','Quantity'])
df['Total Value']=df['Price']*df['Quantity']
print(df)
avegare_price=df['Price'].mean()
exp=df[df['Price']>10000]
print("Most Expensive is\n",exp)
print("Average Price is ",avegare_price)