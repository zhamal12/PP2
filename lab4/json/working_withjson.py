#1 sample-data.json
[
    {"id": 1, "name": "Alice", "score": 85},
    {"id": 2, "name": "Bob", "score": 92},
    {"id": 3, "name": "Charlie", "score": 78}
]

#2
import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

total_score = sum(user["score"] for user in data)
print("Total score:", total_score)

#3
average_score = total_score / len(data)
print("Average score:", average_score)

#4
high_scorers = [user["name"] for user in data if user["score"] > 80]
print(high_scorers)

#5
new_user = {"id": 4, "name": "David", "score": 88}
data.append(new_user)

with open("sample-data.json", "w") as file:
    json.dump(data, file, indent=4)
