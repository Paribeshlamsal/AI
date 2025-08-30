class Car:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def show(self):
        print(f"Hello Car brand is {self.brand} and speed is {self.speed} km/hr")
c1=Car("Toyota",100)
c1.show()