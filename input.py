'''
Home = input("Where is your home: ")
# Home = int(Home)
print(type(Home))
print(Home)

# Below mentioned program I have converted the a and b to int otherwise the average result will not be shown, because str or user input can't be add or devide.
a = input("Enter the 1st Value: ")
b = input("Enter the 2nd Value: ")
a = int(a)
b = int(b)
Average = (a+b)/2
print("The Final value will be: ", Average)
'''

for i in range(8):
    a = input("enter the value {}: ".format(i+1))
    A = int(a*2)
    print('The square value of\n{}'.format(A))