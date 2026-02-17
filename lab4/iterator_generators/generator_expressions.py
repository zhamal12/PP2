#1
gen = (x * 2 for x in range(5))

for val in gen:
    print(val)

#2
gen = (x**2 for x in range(100000))
print(gen)

#3
result = sum(x for x in range(10))
print(result)

#4
gen = (x for x in range(10) if x % 2 == 0)

for val in gen:
    print(val)

#5
gen = (x*y for x in range(3) for y in range(3))

for val in gen:
    print(val)
