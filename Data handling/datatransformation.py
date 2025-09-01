import pandas as pd
df=pd.DataFrame({
    'Score': [85, 70, 78, 92],
    'Grade': ['A', 'B', 'B', 'A']
})
print(df)
df['Score']=df['Score'].map(lambda x:x+5)
print(df)
grade_map={'A':4,'B':3,'C':2}
df['Grade_Numeric']=df['Grade'].map(grade_map)
print(df)
df2 = pd.DataFrame({
    'Math': [85, 90, 78],
    'Science': [88, 92, 81]
})
print(df2)
new_df2=df2.apply(lambda x:x+5)
print(new_df2)
df2['Total']=df2.apply(lambda x: x['Math']+x['Science'],axis=1)
print(df2)
df2_mul=df2[['Math','Science']].applymap(lambda x:x*2)
print(df2_mul)
df3 = pd.DataFrame({
    'Math': [85, 90, 78],
    'Science': [88, 92, 81]
})
df3['Average']=df3.apply(lambda x:(x['Math']+x['Science'])/2,axis=1)
print(df3)
df3['Result']=df3['Average'].apply(lambda x:'Pass'if x >=80 else 'Fail')
print(df3)