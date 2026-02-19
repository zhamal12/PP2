#1
import math

x = int(input())

radian = math.radians(x)
print("{:.6f}".format(radian))

#2
import math

h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value:"))

area = ((a + b)/2) * h
print(area)


#3
n = int(input())
a = int(input())

ap= a / 2
p = n * a

area = (1/2)*p*ap
print(area)

#4
n = int(input())
h = float(input())

area = n * h

print(area)