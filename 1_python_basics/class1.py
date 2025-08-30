class Program:
    def __init__(self, name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print(f"Hello name is {self.name} and age is {self.age} years")

class First(Program):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
    def display(self):
        print(f"Hello grade is {self.grade}")

class Second(Program):
    def __init__(self,name,age,roll):
        super().__init__(name,age)
        self.roll=roll
    def show(self):
        print(f"Hello roll no is {self.roll}")

p1=Program("john",10)
f1=First("Hari",12,"A")
s1=Second("Ram",11,5)
p1.introduce()
f1.introduce()
s1.introduce()
f1.display()
s1.show()