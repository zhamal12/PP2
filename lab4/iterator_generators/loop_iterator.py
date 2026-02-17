#1
numbers = [1, 2, 3]

for num in numbers:
    print(num)

#2
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

#3
mystr = "banana"

for x in mystr:
    print(x)

#4
numbers = [4, 5, 6]
it = iter(numbers)

while True:
    try:
        print(next(it))
    except StopIteration:
        break

#5
mystr = "abcdef"

for x in mystr:
    print(x)