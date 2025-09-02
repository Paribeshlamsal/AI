import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[12,1,14,2,11]
plt.scatter(x,y,color='red',marker='*',s=100,alpha=0.7)
plt.title("Marks vs hours studied")
plt.xlabel("Marks studied")
plt.ylabel("Hours studied")
plt.show()