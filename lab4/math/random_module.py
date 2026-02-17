#1
import random

print(random.random()) #0 до 1

#2
import random

print(random.randint(1, 100))

#3
import random

fruits = ["apple", "banana", "cherry"]
print(random.choice("ABCDEF"))

#4
import random

cards = [1, 2, 3, 4, 5]
random.shuffle(cards)

print(cards)

#5
import random

number = random.randint(1, 5)

guess = int(input("Guess the number 1 to 5: "))

if guess == number:
    print("Correct!")
else:
    print("Not correct. Correct number:", number)
