
# a = ("I have a spokesperson making it in front of white screen for the new Network Eat This Tv")
# a = a.replace ('new','complete new')
# print(a)

# replace gap after of
# a = ("I have a spokesperson making it in front of   white screen for the new Network Eat This Tv")
# a = a.replace('  ', '')
# print(a)
'''

# a = ("I have a spokesperson making it in front of white screen for the new Network Eat This Tv")
# # if = 'it' is after making and before in:
# a = a.replace('it', 'the video')
# print(a)

HOW TO CREATE A FILE IN A DIRECTRY 
MEANING = I WANT TO CREATE A TEXT FILE, TO DESKTOP OR SOMEWHERE ELSE.

'''

# b = "Hello 12345 68952"
# b = b.replace('345', '9')
# print(b)

'''
if there is any double space then it will show the total value , if not then it will show -1

c = "is there any doublespace ?"
c = c.find('  ')
print(c)
'''

# letter = 
# 
'''

Dear <|NAME|>,

Hello,
You are selected. Congradulation.

Thanks & Regards
ABC

date: <|DATE|>

'''
'''
name = input("Enter Your Name: ")
date = input("Enter the Date")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)
'''

filepath1 = '/Users/dev_catalina/Desktop/sample.txt'
filepath2 = '/Users/dev_catalina/Desktop/sa.txt'
filepath3 = '/Users/dev_catalina/Downloads/newcopy.txt'

# Read/Create a file
# fileHandler = open(filepath, 'w')
# print(fileHandler.read())
# fileHandler.close()

# fileHandler = open(filepath, 'w')
# fileHandler.write("Hello this is Code")
# fileHandler.close()


#         "OR"

# with open(filepath2, 'w') as fileHandler:
#     fileHandler.write(" Hello\n My name is Dev\n what's your profession?  Coding is not easy to make.")
# fileHandler.close()
         
with open(filepath1, 'r') as sourceFileHandler:
    with open(filepath3, 'w') as DestinationHandeler:
        for line in (sourceFileHandler):
            DestinationHandeler.write('->{}''Newadded{}{}'.format(line))
   

# with open(filepath2, 'r') as fileHandler:
#     for line in (fileHandler):

