class Animal:
    def speak(self):
        print("BRRRRRRR")
class Dog(Animal):
    def speak(self):
        print("Bhwau bhwau")
a=Animal()
d=Dog()
a.speak()
d.speak()