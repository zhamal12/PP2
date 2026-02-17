#1
import json

data = {
    "name": "Ali",
    "age": 25,
    "city": "Tashkent"
}

with open("data.json", "w") as file:
    json.dump(data, file)

#2
import json

data = {
    "name": "Ali",
    "age": 25,
    "city": "Tashkent"
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

#3
import json

data = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

with open("data.json", "w") as file:
    json.dump(data, file, indent=2)

#4
import json

data = {
    "name": "Linus",
    "age": 30,
    "city": "USA"
}

with open("data.json", "w") as file:
    json.dump(data, file)

#5
import json

data = {
    "name": "Alice",
    "age": 25,
   
}

with open("data.json", "w") as file:
    json.dump(data, file)
