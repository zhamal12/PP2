#1
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#2
bool(False)
bool(None)
bool(0)
bool(0)
bool("")
bool(())
bool([])
bool({})

#3
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

#4
def myFunction() :
    return True

print(myFunction())

#5
def myFunction():
    return True 
if myFunction():
    print("YES")
else:
    print("NO")

x = 200
print(isinstance(x, int))
