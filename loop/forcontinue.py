#1
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)

#2
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#3
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i)

#4
texts = ["Hello", "", "How are you", ""]

for text in texts:
    if text == "":
        continue
    print(text)

#5
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)