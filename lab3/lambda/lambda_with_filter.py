#1
nums = [1, 2, 3, 4, 5, 6]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)

#2
nums = [1, 23, 3, 12, 7, 6]
large = list(filter(lambda x: x > 5, nums))
print(large)

#3
nums = [1, -1, 3, 0, -5, 6]
positive = list(filter(lambda x: x > 0, nums))
print(positive)

#4
words = ["cat", "dog", "elephant", "ant"]
short = list(filter(lambda w: len(w) <= 3, words))
print(short)

#5
nums = [10, 15, 22, 30, 41]
ten_div = list(filter(lambda x: x % 10 == 0, nums))
print(ten_div)  
