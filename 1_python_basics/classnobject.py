class Program:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print(f"Hello name is {self.name} and age is {self.age} years")

p1=Program("John",15)
p1.introduce()