Computer = ["970 Evo", "Hard Drive", "Mouse", "Keyboard", "Internet"] 
'''
it will show the result upto -  Mouse
for C in Computer:
    print(C)
    if C == "Mouse":
        break 

'''
'''
 It will show the result upto -  Hard Drive
for C in Computer:
    if C == "Mouse":
        break
    print(C)

'''    
'''
it will skip the selected variable - Keyboard
for C in Computer:
    if C == "Keyboard":
        continue
    print(C)
'''    
    