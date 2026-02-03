#1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

#2
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x= thisdict.get("model")
print(x)

#3
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)

#4
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()
print(x)

car["color"] = "white"
print(x)

#5
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.values()
print(x)

car["color"] = "white"

print(x)

#6
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()

print(x)

car["year"] = 2020

print(x)

#7
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if "model" in thisdict:
    print("Yes, 'model' is one of the keys in thisdict dictionary")
else:
    print("No")
