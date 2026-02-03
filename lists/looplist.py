#1
thislist = ["apple", "banana", "cherry"]
for i in thislist:
    print(i)

#2
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#3
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

#4
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#5
for x in ["apple", "banana", "cherry"]:
    print(x)