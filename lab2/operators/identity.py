#1
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#2
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

#3
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#4
x = y = [1, 2, 3]

print(x is y)  

#5
a = 1000
b = 1000

print(a == b)  
print(a is b)

