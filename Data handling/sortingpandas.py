import pandas as pd
data = {
    'Name': ['Ram', 'Sita', 'Hari', 'Gita'],
    'Age': [15, 18, 16, 14],
    'Score': [85, 90, 88, 95]
}
df=pd.DataFrame(data)
print(df)#same data
print(df.sort_values(by='Age',ascending=False))#high to low herchha yesle
print(df.sort_index())#after changes it also prints same data
df['Rank']=df['Score'].rank(ascending=False)#naya column thapyo named rank ani score ko aadhar ma rank diyo 1 2 3 4 vanera
print(df)
print(df.sort_values(by=['Name','Score'],ascending=[True,False]))
print(df.sort_values(by='Rank',ascending=True))