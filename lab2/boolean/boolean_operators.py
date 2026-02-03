#1 and
age = 20
has_passport = True 

result = age >= 18 and has_passport
print(result)

#2 or
is_student = False
has_discount = True

print(is_student or has_discount)

#3 not
is_raining = True

print(not is_raining)

#4
age = 16
has_permission = True

can_enter = (age >= 18) or (age >= 16 and has_permission)
print(can_enter)

#5
login = "admin"
password = "1234"

if login == "admin" and password == "1234":
    print("Pass")
else:
    print("Not pass")
