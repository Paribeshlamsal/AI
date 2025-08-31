import pandas as pd
total=[
    ['ClassA','Ram',15000,'15'],
    ['ClassB','Hari',25000,'10'],
    ['ClassA','Shyam',20000,'12'],
    ['ClassB','Gopal',21000,'14']
]
df=pd.DataFrame(total,columns=['Class','Name','Salary','Age'])
grouping=df.groupby('Class')['Salary'].sum()
print("Total salary according to class is \n",grouping)