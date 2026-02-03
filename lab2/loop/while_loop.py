#1
i = 1
while i < 6:
    print(i)
    i += 1


#2
password = ""

while password != "1234":
    password = input("Enter password:")

print("Welcome!")

#3
n = int(input())
total = 0

while n > 0:
    total += n 
    n -= 1

print("Sum:", total)

#4
numbers = [10, 20, 30, 40]
i = 0

while i < len(numbers):
    print(numbers[i])
    i += 1

#5
n = int(input())
total = 0

while n > 0:
    total += n % 10
    n //= 10

print("Summa:",total)