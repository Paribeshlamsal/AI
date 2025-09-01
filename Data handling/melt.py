import pandas as pd
data = {
    'Student': ['Alice', 'Bob'],
    'Math': [78, 65],
    'Science': [85, 70],
    'English': [92, 75]
}
df=pd.DataFrame(data)
print(df)
df_melt=pd.melt(df,id_vars=['Student'],var_name='Subject',value_name='Marks')
print(df_melt)