#1
class A:
    def method_a(self):
        print("Method A")

class B:
    def method_b(self):
        print("Method B")

class C(A, B):
    pass

c = C()
c.method_a()
c.method_b()

#2
class Swimmer:
    def swim(self):
        print("Swim")

class Walker:
    def walk(self):
        print("Walk")

class Frog(Swimmer, Walker):
    pass

f = Frog()
f.swim()
f.walk()

#3
class Father:
    def __init__(self):
        print("Father constructor")

class Mother:
    def __init__(self):
        print("Mother constructor")

class Child(Father, Mother):
    pass

c = Child() 

#4
class A:
    def show(self):
        print("Class A")

class B:
    def show(self):
        print("Class B")

class C(A, B):
    pass

c = C()
c.show()  

#5
class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    def greet(self):
        super().greet()

c = C()
c.greet() 


