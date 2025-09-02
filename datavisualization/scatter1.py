import matplotlib.pyplot as plt
hours=[1,2,3,4,5]
marks_maths=[90,55,70,80,50]
marks_science=[60,70,40,99,80]
plt.scatter(hours,marks_maths,color='blue',marker='s',s=100,label='Maths')
plt.scatter(hours,marks_science,color='red',marker='o',s=100,label='Science')
plt.title("Marks vs hours")
plt.xlabel("Hours studied")
plt.ylabel("Marks Scored")
plt.grid(True,linestyle=':')
plt.legend()
plt.show()