
num=int(input("Enter a no: "))

for n in range(num):
    counter = n+1
    if(num % counter == 0):
        # counter is a factor of num
        if counter % 2 == 0:
            # factor is a even number
            print('{:20} {:-3}'.format('Even factor',counter))
        else:
            # factor is a odd number
            print('{:20} {:-3}'.format('Odd factor',counter))



num=50
for i in range(1,num+1):
    rem=num%i
    if(rem==0):
        if(i%2==0):
            print("Factor is even:",i)
        else:
            print("factor is odd: ",i)
    else:
        pass