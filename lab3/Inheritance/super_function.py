#1
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

s = Student("Ali", 5)
print(s.name)   
print(s.grade)  

#2
class Animal:
    def speak(self):
        print("animal make sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Gaf!")

d = Dog()
d.speak()

#3
class Worker:
    def work(self):
        print("working")

class Programmer(Worker):
    def work(self):
        super().work()
        print("write code")

p = Programmer()
p.work()

#4
class Car:
    def __init__(self, brand):
        self.brand = brand

class ElectricCar(Car):
    def __init__(self, brand, battery):
        super().__init__(brand)
        self.battery = battery

e = ElectricCar("Tesla", "75kWh")
print(e.brand)
print(e.battery)

#5
class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        super().show()
        print("Class B")

b = B()
b.show()



