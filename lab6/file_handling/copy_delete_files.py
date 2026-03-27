import os
os.remove("simple.txt") 

# Check if file exists, then delete it:
import os
if os.path.exists("simple.txt"):
  os.remove("simple.txt")
else:
  print("The file does not exist") 

# Remove the folder "myfolder":
import os
os.rmdir("myfolder") 