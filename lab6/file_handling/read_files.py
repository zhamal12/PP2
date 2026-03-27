# reading lines from a file
f = open("simple.txt")
print(f.read()) 

# Using the with keyword:
with open("simple.txt") as f:
  print(f.read()) 
f.close() 

# Return the 5 first characters of the file:
with open("simple.txt") as f:
  print(f.read(5)) 

# Read one line of the file:
with open("simple.txt") as f:
  print(f.readline()) 