import matplotlib.pyplot as plt
x=[1,2,3,4,5]
chocolates=[2,4,6,8,10]
icecream=[1,3,5,7,9]
plt.plot(x,chocolates,label="Chocolates",marker='o',markerfacecolor='green')
plt.plot(x,icecream,label="IceCream",marker='*',markerfacecolor='red')
plt.title("Snacks over Days")
plt.xlabel("Day")
plt.ylabel("Quantity Eaten")
plt.legend()
plt.show()

