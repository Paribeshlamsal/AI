import pandas as pd
scores=[78,85,92,66,90]
s=pd.Series(scores,index=['Alice', 'Bob', 'Charlie', 'David', 'Eva'])
print(s['Charlie'])
print(s[s>80])
