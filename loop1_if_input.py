'''
colors = [ 'Red', 'Green', 'Blue' ]
Blue = 'remote'
Red  = 'mouse'
Green = 'cardreader'

C = input ("Please Choose a color: " )

# for c in colors:
#     print(C)

if not C in colors:
    print("Wrong Color Typed") 
else:
    if C == 'Green':
        print("cardreader")
    elif C == 'Blue':
        print("remote")
    elif C == 'Red':
        print("mouse")
    # else:
    #     print("not sure")

'''


a = ["Dev", "Avik", "Saikat", "Sachin", "Sourav"]
for name in a:
    if name.startswith ("S"):
        print("Hello " + name)
