#1
class Animal:
  def speak(self):
    print("say sound")

class Dog(Animal):
  pass

dog = Dog()
dog.speak()

#2
class Animal:
    def speak(self):
        print("say sound")

class Cat(Animal):
    def speak(self):
        print("Meow")

cat = Cat()
cat.speak()  

#3
class A:
    def hello(self):
        print("Hello")

class B(A):
    pass

b = B()
b.hello()

#4
class A:
    x = 10

class B(A):
    pass

b = B()
print(b.x)

#5
class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

b = B()
b.show()

