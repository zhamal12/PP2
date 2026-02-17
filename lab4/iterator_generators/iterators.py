#1
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#2
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#3
numbers = [10, 20, 30]
it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))

#4
numbers = [1, 2]
it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))  #Error

#5
text = "ABC"
it = iter(text)

print(next(it))  
print(next(it))  
print(next(it))  




