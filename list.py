# l1 = [1,5,8,10,15,20,3,100]
# print(l1)

# l1.sort() #sort the list [1, 3, 5, 8, 10, 15, 20, 100]
# print(l1)

# l1.append(200) #add at the end - [1, 3, 5, 8, 10, 15, 20, 100, 200]
# print(l1)

# l1.reverse() # it will print reverse order [100, 3, 20, 15, 10, 8, 5, 1]
# print(l1)

# l1.insert(0, 36) #it will print 36 instead of 1 
'''
[1,5,8,10,15,20,3,100]
(0,1,2, 3, 4, 5,6,  7)
'''
# print(l1)

'''
Colors = ("Red", "Green", "Blue")
C = input("Enter the Color: ")
if C in Colors:
    print("Yes, its Present")
else:
    print("Not Present")

'''
'''
f1 = input("Enter Frouit No1: ")
f2 = input("Enter Frouit No2: ")
f3 = input("Enter Frouit No3: ")
f4 = input("Enter Frouit No4: ")
f5 = input("Enter Frouit No5: ")
f6 = input("Enter Frouit No6: ")
f7 = input("Enter Frouit No7: ")

FrouitList = [f1, f2, f3, f4, f5, f6, f7]
print(FrouitList)

'''

# Sumno = [10, 15, 16, 17]
# print(sum(Sumno))

# a = (1, 2, 0, 0, 6 )
# print(a.count(0))

# tuple cant change
# a = (2,3,5,3)
# a[0] = 13

# a = [3,5,5,7,8]
# print(sum(a))

# language =["Go", "Python"]
# language =("Go", "Python")
# print(language *3)

# print("Go" in language, "Ruby" in language) # it will show :Go = True and Ruby = False 

# print(language + ["PHP", "C++"]) # it will add PHP and C++ with GO and Python
# print(language + ["PHP", "C++"]) # it will Not add PHP and C++ with GO and Python because its tuple= language =("Go", "Python")

list = [x**2 for x in [1,2,3,4,5]]
print(list)   # list will be print after multiplying with 2 

# to reverse
Computer = ["Ram", "HD", "Monitor", "Keyboard"]
print(Computer[::-1])