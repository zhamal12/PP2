#1 append()- добавить элемент в конец списка
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#2 insert()-вставить элемент списка в заданный индекс
thislist = ["apple", "banana", "cherry"]
thislist.insert(1,"orange")
print(thislist)

#3 extend()-добавить элементы из другого списка в текущий список
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#4
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#5
mylist = ["apple", "banana", "cherry"]
mylist.insert(0, 'orange')
print(mylist[1])