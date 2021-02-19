num = int(input("Enter the number: "))
'''
for i in range(1, 11):
    # print(str(num) + "X" + str(i) + "=" + str(num*i))
    print(f"{num}X{i}={i*num}")

'''
i=0
while i<=num:  #use for loop to iterates 1 times
    i+=1
    print(str(num) + "X" + str(i) + "=" + str(num*i))