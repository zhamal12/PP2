#1
for i in range(1, 10):
    if i == 5:
        break
    print(i)

#2
numbers = [3, 6, 9, 12, 15]

for i in numbers:
    if i == 9:
        print("9!")
        break 

#3
password = ["123", "admin", "python", "qwerty"]
for i in password:
    if i == "python":
        print("Correct!")
        break

#4
nums = [5, 8, 4, -1, 9]

for n in nums:
    if n < 0:
        print("Negative number")
        break

#5
secret = 7

for i in range(1, 20):
    print("Check:", i)
    if i == secret:
        print("Correct")
        break