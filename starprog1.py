'''
n = 3

for i in range (3):
    print("*" * (i+1))

# output
*
**
***

'''


# n = 4

'''
for i in range(1,5):
    for j in range(1,5):
        if j<= 5-i:
            print("*", end='')
        else:
            print(" ", end='')
    print()
    
'''
for i in range(1,5):
    for j in range(1,9):
        if j>= 5-i and j<=3+i:
            print("*", end='')
        else:
            print(" ", end='')
    print()
