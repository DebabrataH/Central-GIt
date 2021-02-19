'''
sentence = input("User input words: ")
# to create the input as list but seperate comma
chars = list(sentence)
letters = 0
digits = 0

# isalpha = to check if any alphabate is here 
# isdigit = to check if any digit is here
for c in chars:
    if c.isalpha():
        letters += 1
    elif c.isdigit():
        digits += 1

print("LETTERS:{}".format(letters))
print("DIGITS:{}".format(digits))

'''



s = “aac34520”
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])

