#1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#2 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list1:
    list2.append(x)
print(list2)

#3
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#4
thislist = ["apple", "banana", "cherry"]
mylist = [10, 20, 30]
thislist.extend(mylist)
print(thislist)

#5
thislist = ["apple", "banana", "cherry"]
mylist = [10, 20, 30]

for x in mylist:
    thislist.append(x)
print(thislist)