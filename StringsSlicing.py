'''
Title = "Hello Dev"
Greeting = "How r u ?"

# Concatinating two Str.
Combindly = Title + Greeting
print(Combindly)

print(Title[5])   
# (Hello Dev = 01234 5 678) because Length=8 
# (H  e  l  l  o     D  e  v
# -9 -8 -7 -6 -5 -4 -3 -2 -1)
c = Title [-9:]
print(c)
print(Title[2:7]) # ( : means 2 to 7 but python will cound upto 6 , won't be count.)
print(Title[0:])  # That's mean it will count 0 to till end no.
print(Title[:8])  # that's mean it will count from 0 to 8.

#Str Skip value
A = "Remote"
print(A[0: : 2])  # 2 means it will print 1 letter and skip 1 letter (Remote)

# Strings Functions 
Hackintosh = "it's very easy to install now a days"

print(len(Hackintosh))  # it will print the total no to charecter including space = 36
print(Hackintosh.endswith("a days")) # if the sentence will end "a days" it will print True else False.3
print(Hackintosh.count("s")) # it will count how many times "s" has been used.
print(Hackintosh.count("now")) # it will count how many times "now" word used.
print(Hackintosh.capitalize()) # Capitalize() function will make the 1st letter capital.
print(Hackintosh.replace("easy", "difficult")) 
''' 
# it will replace the easy word to difficult, 
#     no matter how many times i used that word '''

# Escape Secuence (\n means it will print in second line)
A = "I am Debabrata. \nI am learning python"
print(A)

# \t means it will create a TAB after "am".
B = "Python is not easy to learn, but I am \ttrying to learn"
print(B)  
   
'''
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab

'''

# To make all capital 

Dev = 'video editor'
print(Dev.upper())

'''


Name = "Dev"
Age = 35

# print("My name is %s and my age is %d" % (Name, Age)
# print("My name is " + Name + " and my age is " + str(Age))