#1
def my_function():
    print("Hello from a function")

my_function()
my_function()

#2
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 10 / 5

print(fahrenheit_to_celsius(33))
print(fahrenheit_to_celsius(50))

#3
def get_greeting():
    return "Hello from a function"

message = get_greeting()
print(message)

#4
def get_greeting():
    return "Get greeting"
print(get_greeting())

#5
def my_function():
    pass
