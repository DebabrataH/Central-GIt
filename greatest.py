a = int(input("Enter 1st no: "))
b = int(input("Enter 2nd no: "))
c = int(input("Enter 3rd no: "))
d = int(input("Enter 4th no: "))
# e = int(input("Enter 5th no: "))

if (a > d):
    num1 = a
else:
    num1 = d

if (b > c):
    num2 = b 
else:
    num2 = c

if (num1 > num2):
    print(str(num1) + " is Greatest")

else:
    print(str(num2) + " is Greatest")