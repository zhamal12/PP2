#1
nums = [1, 2, 3, 4, 5]
power = list(map(lambda x: x * x, nums))
print(power)

#2
nums = [1, 2, 3, 4]
numbers = list(map(lambda x: x * 10, nums))
print(numbers)

#3
nums = [1, 2, 3, 4]
strs = list(map(lambda x: str(x), nums))
print(strs)

#4
a = [1, 2, 3]
b = [4, 5, 6]
summa = list(map(lambda x, y: x + y, a, b))
print(summa)

#5
words = ["hello", "world", "python"]
word = list(map(lambda w: w.upper(), words))
print(word)