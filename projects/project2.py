import pandas as pd
import numpy as np
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [78, 65, 90, 55, 88],
    'Science': [85, 70, 95, 60, 80],
    'English': [92, 75, 85, 50, 90]
}
df=pd.DataFrame(data)
print(df)
df['Total Marks']=df['Math']+df['Science']+df['English']
df['Average Marks']=(df['Math']+df['Science']+df['English'])/3
df['Pass']=(df['Math']>=60)&(df['Science']>=60)&(df['English']>=60)
print(df)