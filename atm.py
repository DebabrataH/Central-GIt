from getpass import getpass
pin = getpass("User input PIN: ")
print('''
1. Check balance
2. Make a withdrawl
''')
selection = int(input("Enter number: "))
if selection==1:
    print(1000)