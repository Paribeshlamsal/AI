import pandas as pd

df = pd.DataFrame({
    'Color': ['Red', 'Blue', 'Green', 'Red', 'Blue'],
    'Value': [100, 200, 150, 120, 180]
})

print("Original DataFrame:")
print(df)
df_encoded=pd.get_dummies(df,columns=['Color'],dtype=int)
print("After encoding \n")
print(df_encoded)