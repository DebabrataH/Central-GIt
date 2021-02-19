s1 = "Math"
s2 = "Eng"
s3 = "Beng"

subject1 = int(input("Enter the 1st mark: "))
subject2 = int(input("Enter the 2nd mark: "))
subject3 = int(input("Enter the 2nd mark: "))
subject4 = int(input("Enter the 4th mark: "))

if (subject1 or subject2 or subject3 or subject4) < 30:
    print("You are failled due to lessthan 30")

elif (subject1 + subject2 + subject3 + subject4) / 4 < 40 :
    print("You are failled due to total percentage is less than 40")

else:
    print("You are passed")