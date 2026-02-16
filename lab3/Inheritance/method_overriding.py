#1
class Animal:
    def speak(self):
        print("animal make sound")

class Dog(Animal):
    def speak(self):
        print("Gaf!")

dog = Dog()
dog.speak()   

#2
class Shape:
    def area(self):
        print("area unknown")

class Square(Shape):
    def area(self):
        print("square area")

s = Square()
s.area()  

#3
class Person:
    def work(self):
        print("human working")

class Teacher(Person):
    def work(self):
        print("teacher study")

t = Teacher()
t.work()   

#4
class Vehicle:
    def move(self):
        print("transport going")

class Bike(Vehicle):
    def move(self):
        print("bike going")

b = Bike()
b.move() 

#5
class Bird:
    def sound(self):
        print("birds make sound")

class Parrot(Bird):
    def sound(self):
        print("popugai talking")

p = Parrot()
p.sound()   

