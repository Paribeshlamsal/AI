import pandas as pd

data = {
    'Student': ['Alice', 'Bob'],
    'Math': [78, 65],
    'Science': [85, 70],
    'English': [92, 75]
}
df=pd.DataFrame(data)
df.set_index('Student',inplace=True)
print(df)
after_stack=df.stack()
print("After stacking \n")
print(after_stack)
after_unstack=after_stack.unstack()
print("After unstacking \n")
print(after_unstack)