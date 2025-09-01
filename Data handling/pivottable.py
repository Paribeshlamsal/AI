import pandas as pd
data = {
    'Student': ['A', 'B', 'C', 'A', 'B', 'C'],
    'Subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science'],
    'Marks': [85, 78, 92, 88, 74, 95]
}
df=pd.DataFrame(data)
pivot=pd.pivot_table(df,values='Marks',index='Subject',aggfunc='mean')
print(pivot)
pivot2=pd.pivot_table(df,values='Marks',index='Student',columns='Subject',aggfunc='mean')
print(pivot2)
pivot3=pd.pivot_table(df,values='Marks',index='Student',columns='Subject',aggfunc=['mean','max','min'])
print(pivot3)
df.loc[6]=['D','Math',None]
pivot4=pd.pivot_table(df,values='Marks',index='Subject',aggfunc='mean',fill_value=0)
print(pivot4)
