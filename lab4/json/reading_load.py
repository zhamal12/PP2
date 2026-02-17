#1
import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data)

#2
import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data["name"])

#3
import json

with open("data.json", "r") as file:
    users = json.load(file)

for user in users:
    print(user["id"], user["name"])

#4
import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data["name"])

#5
import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data[0])
