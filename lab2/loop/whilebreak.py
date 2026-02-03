#1
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#2
while True:
    n = int(input())
    if n == 0:
        break
    print("Number:", n)

#3
while True:
    password = input("Password: ")
    if password == "python":
        break
print("Welcome!")

#4
while True:
    n = int(input())
    if n < 0:
        break
    print(n)

#5
secret = 7
while True:
    n = int(input())
    if n == secret:
        print("Correct!")
        break