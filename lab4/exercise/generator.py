#1
def my_generator(N):
    for i in range(1, N + 1):
        yield i **2


N = int(input())
g = my_generator(N)

for x in g:
    print(x) 

#2
def my_generator(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i
     
n = int(input())
g = my_generator(n)

print(",".join(str(num) for num in g))

#3
def my_generator(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())

for val in my_generator(n):
    print(val)

#4
def my_generator(a, b):
    for i in range(a, b):
        yield i**2

a = int(input())
b = int(input())

squares = my_generator(a, b)
for val in squares:
    print(val, end=" ")

#5
def my_generator(n):
    for i in range(n, 0, -1):
        yield i

n = int(input())
for num in my_generator(n):
    print(num, end= " ")