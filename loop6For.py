# for letter in ("debabrata"):
#     print("The letter is", letter)

# for num in (10,20,30,40):
#     print(num)

# count = 0 
# for i in range (4):
#     while i<=2:
#         if i==2:
#             break
#         count = count+10
#         i=i+1
#     else:
#         count = count+1
# else:
#     count = (count+20)
# print(count)

# user = int(input("Enter the number of rows:"))
# for i in range(0,user):
#     for j in range(0,user-i-1):
#         print(end=" ")
#     for j in range(0,i+1):
#         print("*",end=" ") 
#     print()

for i in range(10):
    if (i+1) % 2 != 0: # allow only even number
        for j in range(10):
            print('{:2} x {:2} : {:3}'.format(i+1, j+1, ((i+1)*(j+1))))
        userInput = input('next')
        if userInput!='n':
            break