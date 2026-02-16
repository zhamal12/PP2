#1
def sum(a, b):
    return a + b

print(sum(3, 2))

#2
def summa(a, b):
    return a + b

result = summa(10, 34)
print(result)

#3
def summa(a, b):
    return a + b

def kobeitu(a, b):
    print(a * b)

result = kobeitu(summa(2, 3), 4)
print(result)

#4
def max_number(a, b):
    if a > b:
        return a
    else:
        return b
    
print(max_number(5, 9))

#5
def summa(lst):
    result = 0
    for i in lst:
        result += i
    return result

print(summa([1,2,3,4]))