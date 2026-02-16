#1
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

#2
def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

#3
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

#4
def power(x):
   return x * x

power2 = lambda x : x * x

print(power(6))
print(power2(4))

#5
def maxx(a, b):
   if a > b:
      return a
   else:
      return b
   
maxx2 = lambda a, b: a if a > b else b

print(maxx(21, 45))
print(maxx2(33, 24))