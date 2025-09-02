import matplotlib.pyplot as plt
fruits=['Apple','Banana','Cherry','Dates']
counts=[10,45,3,77]
plt.bar(fruits,counts)
plt.title("Number of fruits in each bar")
plt.xlabel("Fruits type")
plt.ylabel("Counts")
plt.show()