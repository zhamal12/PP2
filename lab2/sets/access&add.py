#1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

#2
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#3
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

#4
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

#5
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)