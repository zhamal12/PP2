#1
nums = [5, 2, 9, 3, 1, 8]
sorted_num = sorted(nums)
print(sorted_num)

#2
nums = [5, 2, 9, 3, 1, 8]
reversed_num = sorted(nums, reverse=True)
print(reversed_num)

#3
words = ["cat", "elephant", "dog", "ant"]
length = sorted(words, key=lambda w: len(w))
print(length) 

#4
words = ["cat", "elephant", "dog", "ant"]
end_alph = sorted(words, key=lambda w: w[-1])
print(end_alph)

#5
nums = [-10, 2, -3, 7, 5]
module_num = sorted(nums, key=lambda x: abs(x))
print(module_num) 
