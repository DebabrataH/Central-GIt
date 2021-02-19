'''

input_num = input("User input number: ")
reverse = input_num[::-1]
if input_num == reverse:
    print('It is a palindrome')
else:
    print('It is mot a palindrome')
    
'''


# change this value for a different output
my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str.casefold()

# reverse the string
rev_str = reversed(my_str)

# check if the string is equal to its reverse
if list(my_str) == list(rev_str):
    print("It is palindrome")
else:
    print("It is not palindrome")