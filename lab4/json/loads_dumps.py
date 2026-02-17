#1
import json

json_string = '{"name": "Ali", "age": 25}'

data = json.loads(json_string)
print(data)
print(type(data))

#2
import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)

print(y["age"])

#3
import json

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

y = json.dumps(x)

print(y)

#4
import json

data = {
    "name": "Ali",
    "age": 25
}

json_string = json.dumps(data)
print(json_string)

#5
import json

data = {"name": "Ali", "age": 25, "city": "Tashkent"}

json_string = json.dumps(data, indent=4)
print(json_string)
