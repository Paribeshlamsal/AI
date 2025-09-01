import pandas as pd
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Math': [78, 65, 90, 88, 95],
    'Science': [85, 70, 95, 80, 100],
    'English': [92, 75, 88, 85, 90]
}
df=pd.DataFrame(data)
print(df)
df['Total']=df['Math']+df['Science']+df['English']
df['Average']=df['Total']/3
top_scorer=df.loc[df['Total'].idxmax()]
print(top_scorer)
average_per=df[['Math','Science','English']].mean()
print(average_per)
sorted_df=df.sort_values(by='Total',ascending=False)
print(sorted_df)
df.to_csv('students_analytics.csv',index=False)
df.to_excel('students_report.xlsx',index=False)
print("\n DataFrame saved to 'students_analytics.csv'")
print("\n DataFrame saved as 'students_report.xlsx'")
