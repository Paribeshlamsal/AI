import pandas as pd
data = {
    'Date': ['2025-09-01', '2025-09-02', '2025-09-03','2025-09-04','2025-09-05'],
    'Sales': [200, 250, 300,400,350]
}
df=pd.DataFrame(data)
df['Date']=pd.to_datetime(df['Date'])
print(df)
print(df.dtypes)
df['Year']=df['Date'].dt.year
df['Month']=df['Date'].dt.month
df['Day']=df['Date'].dt.day
df['Weekday']=df['Date'].dt.day_name()
df['Month Name']=df['Date'].dt.month_name()
print(df)
df.set_index('Date',inplace=True)
weekly_sales=df['Sales'].resample('ME').sum()
print(weekly_sales)