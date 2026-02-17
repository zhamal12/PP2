#1
def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()

print(next(g))
print(next(g))
print(next(g))

#2
def numbers():
    for i in range(5):
        yield i

for n in numbers():
    print(n)

#3
def squares(n):
    for i in range(n):
        yield i * i
    
for s in squares(5):
    print(s)

#4
def infinite():
    n = 1
    while True:
        yield n 
        n += 1

for num in infinite():
    if num > 5:
        break
    print(num)


#5
def gen1():
    yield 1
    yield 2

def gen2():
    yield from gen1()
    yield 3
