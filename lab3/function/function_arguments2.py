#1
def my_function(fruits):
    for fruit in fruits:
        print(fruit)
    
my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)


def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {"name": "Emil", "age": 24}
my_function(my_person)

#2
def my_function(x, y):
    return x + y

result = my_function(5, 10)
print(result)


def my_function():
    return["apple", "banana", "cherry"]

fruits = my_function()
print(fruits)
print(fruits[0])
print(fruits[2])

#3
def my_function():
    return(10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

def my_function(name, /):
    print("Hello", name)

my_function("Emil")

def my_function(name):
    print("Hello", name)
my_function("Emil")

#4
def my_function(*, name):
    print("Hello", name)

my_function(name="Emil")

#5
def my_function(a, b, /, *, c, d):
    return a + b + c + d

result = my_function(5, 10, c = 12, d = 20)
print(result)