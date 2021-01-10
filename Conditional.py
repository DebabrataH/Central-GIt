import os
import shutil
import fileinput
import os.path
from os import path

# a = input("Enter a value: ")
# a = int(a)
# if a>22:
#     print("Greater")
    
# elif a>20: 
#     print("Smaller")   
# else:
#     print("Wrong")

    # New program

# Declare variables

SourcePath = "../../../../Downloads/MultiBeast 12.3.0 Catalina Edition"
DestinationPath = "../../MultiBeast 12.3.0 Catalina Edition"
DestinationPath2 = "/Users/dev_catalina/Desktop/Catalina Edition" # (I have change the Folder name only)

if not os.path.exists(DestinationPath2):
    if os.path.exists (SourcePath):
        shutil.copytree(SourcePath, DestinationPath2)
    else:
        print("there is no such file exit")

# I want to know if the Folder already exit then it will shown Already Exit. How to do ?


