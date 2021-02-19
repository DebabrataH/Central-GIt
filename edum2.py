import os
from cryptography.fernet import Fernet

# username = input("Enter the User Name: ")
# Password = input("Enter the Passowrd: ")


    

'''
1.What is the output of the following code?

# it will show 4 because set doesn't count duplicate nos.
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))

2.What will be the output?

# it will print ['john', 'peter'], its a dictionary .
d ={"john":40, "peter":45}
print(list(d.keys()))

'''

'''
4.Write a for loop that prints all elements of a list and their position in the list.

a = [4,7,3,2,5,9]

a = [4,7,3,2,5,9]

for p in a: 
    # print("No: " + str(p) + " Index: "+ str(a.index(p)))
    
    # print(p)
    # print(a.index(p))
    print("{} Position {}".format(p,a.index(p)))
'''

'''
5.Please   write   a   program   which accepts  a   string   from   console   and   print   the characters that have even indexes.

H1e2l3l4o5w6o7r8l9d
Helloworld


uinput = input( " Enter the text:")

if uinput:
	string = ""
	for i in uinput:
		if uinput.index(i)%2 == 0:
			string += str(i)
	
	print(string)

    OR

text = "H1e2l3l4o5w6o7r8l9d"
ns =''
for i in range(len(text)):
    if i % 2 == 0:
        ns+=text[i]
print(ns)

'''

'''
6.Please write a program which accepts a string from console and print it in reverse order.

uinput = input( " Enter the text:")
print(uinput[:: -1])
'''

'''
7.Please write a program which count and print the numbers of each character in a string input by console.

word = "abcdefgabc"
Alphabet=list(word)
# declare an dictonary, hashmap or associstive array
counts = {}

for char in Alphabet:
    counts[char] = counts.get(char, 0) + 1
    
for k,v in counts.items():
    print("{},{}".format(k,v))
        
    '''
    

'''


With   two   given   lists   [1,3,6,78,35,55]   and   
[12,24,35,24,88,120,155],   write   a program to make a list whose elements are intersection of the above given lists.

lst1 = [1,3,6,78,35,55]
lst2 = [12,24,35,24,88,120,155]


'''


'''
With a given list [12,24,35,24,88,120,155,88,120,155] write a program to print this 
list after removing all duplicate values with original order reserved

lista = [18,20,12,12,13,14,15]
print(list(set(lista)))  # but this is not showing original order

'''


'''
By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155]

lists = [12,24,35,24,88,120,155]
newlist = [x for x in lists if x != 24]
print(newlist)
'''

'''

list1= [12,24,35,24,88,120,155,88,120,155]
uniqueList = []
for x in list1:
    if not x in uniqueList:
        uniqueList.append(x)

print(uniqueList)
'''
'''
question = 14


n = int(input('Enter a number: '))
rseult = 0.0
for x in range(n):
    t = float(x + 1)
    rseult = rseult + t/(t+1)

print(rseult)

'''
'''
specialCharAllowed = ['-', '/', '_']
referenceID = str(input('Input reference ID: '))
if len(referenceID) != 12:
    print('Not a valid reference ID')
else:
    hasInvalidChar = False
    for c in referenceID:
        if not (c.isalpha() or c.isdigit() or (c in specialCharAllowed)):
            hasInvalidChar = True
            break
    
    if hasInvalidChar:
        print('This is not a valid reference ID')
    else:
        f = Fernet(Fernet.generate_key())
        encryptedReferenceID = f.encrypt(bytes(referenceID, 'utf-8'))
        print(encryptedReferenceID)
'''


# By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155]

# lists = [12,24,35,24,88,120,155]
# newlist = [x for x in lists if x != 24]
# print(newlist)

# # 14. Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0).
# n = int(input('Enter a number: '))
# rseult = 0.0
# for x in range(n):
#     t = float(x + 1)
#     rseult = rseult + t/(t+1)


# 9.With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.

list1= [12,24,35,24,88,120,155,88,120,155]
uniqueList = []
for x in list1:
    if not x in uniqueList:
        uniqueList.append(x)

print(uniqueList)