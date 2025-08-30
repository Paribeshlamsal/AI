import pandas as pd
numbers=[1,2,3,4,5]
s=pd.Series(numbers)
print(s)
s1=pd.Series(numbers,index=['a','b','c','d','e'])
print(s1)
print(s1['c'])
print(s[4])
print(s[s>=2])