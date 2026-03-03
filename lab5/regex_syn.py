#1 start with and end
import re 

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("Yes! We have a match")
else:
    print("No match")

#2 Find all lower case characters 
#alphabetically between "a" and "m":
import re 

txt = "The rain in Spain"

x = re.findall("[a-m]", txt)
print(x)

#3 Find all digit characters:
import re

txt = "That will be 59 dollars"

x = re.findall("\d", txt)
print(x)

#4
import re 
txt = "hello planet"

x = re.findall("he..o", txt)
print(x)

#5
import re

txt = "hello planet"

#Check if the string starts with 'hello':

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")

#6
import re

txt = "hello planet"

#Check if the string ends with 'planet':

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
