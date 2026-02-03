#1
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#2
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

#3
fruits = ("apple", "papaya", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#4
thistuple = ("apple", "banana", "chery")
for x in thistuple:
    print(x)

#5
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

#6
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

n = int(input())

summa = 0
for i in range(1, n):
    summa += i
print(summa)