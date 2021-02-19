num = int(input("Enter the no: "))
prime  = True
for i in range(2, num):
    if (num%i == 0):
        prime  = False
        break
if prime:
    print("Prime")
else:
    print("not prime")

     
        