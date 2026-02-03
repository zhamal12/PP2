#1
i = 0
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

#2
while True:
    n = int(input())
    if n == 0:
        break
    if n < 0:
        continue
    print("Positive number:",n)

#3
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

#4
i = 1
while i <= 10:
    if i % 3 == 0:
        i += 1
        continue
    print(i)
    i += 1

#5
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)