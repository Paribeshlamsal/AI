import matplotlib.pyplot as plt
fruits=['Dates','Apples','Mangoes','Grapes']
jar_a=[25,66,12,76]
jar_b=[70,45,71,11]
bar_width=0.4
import numpy as np
x=np.arange(len(fruits))
plt.bar(x-bar_width/2,jar_a,width=bar_width,label="Jar A",color='red')
plt.bar(x+bar_width/2,jar_b,width=bar_width,label="Jar B",color='skyblue')
plt.title("Total no of counts of fruits")
plt.xlabel("Fruits")
plt.ylabel("Counts")
plt.xticks(x,fruits)
plt.legend()
plt.show()