import matplotlib.pyplot as plt
import numpy as np
days=[1,2,3,4,5]
chocolates=[2,3,4,5,6]
icecream=[3,4,2,5,6]

fruits=['Apple','Banana','Date','Orange']
counts_a=[33,44,2,1]
counts_b=[44,33,66,7]

hours=[1,2,3,4,5]
marks_math=[33,44,55,66,44]
marks_science=[66,75,77,89,99]

plt.figure(figsize=(12,6))

plt.plot(days,chocolates,label='Chocolates',marker='*',linestyle='--',color='violet',linewidth=2)
plt.plot(days,icecream,label='Icecream',marker='s',color='green',linewidth=2)

bar_width=0.5
x=np.arange(len(fruits))
plt.bar(x-bar_width/2,counts_a,width=bar_width,label='Jar A',color='red')
plt.bar(x+bar_width/2,counts_b,width=bar_width,label='Jar B',color='blue')
plt.xticks(x,fruits)

plt.scatter(hours,marks_math,label='Maths',alpha=0.7,marker='s',color='purple')
plt.scatter(hours,marks_science,label='Science',alpha=0.7,marker='o',color='orange')

plt.title("Line+Bar+Scatter")
plt.xlabel("X-axis(Categories & time)")
plt.ylabel("Values")
plt.grid(True,linestyle=':')



plt.legend()
plt.tight_layout()
plt.show()