list_even_digit_num = []

for n in range(1000, 3001):
    num_as_str = str(n)
    digits_in_num = list(num_as_str)
    num_has_odd_digit = False
    # check for each digit
    for d in digits_in_num:
        if int(d) % 2 != 0:
            # first odd digit found
            num_has_odd_digit = True
            break
    
    if not num_has_odd_digit:
        list_even_digit_num.append(str(n))

print(",".join(list_even_digit_num))




'''
values = []
for i in range(1000,3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and
    (int(s[3])%2==0):
        print(values.append(s))
    print (",".join(values))
'''