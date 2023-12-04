"""Prints whether a password is strong or weak"""
password = input("Enter new password: ")



# Check if password is: greater than 8 chars, has an uppercase letter, and has a digit
checker = {"has_digit":False}
for i in password:
    if i.isdigit():
        checker["has_digit"] = True

if len(password) >= 8:
    checker["8chars"] = True
else:
    checker["8chars"] = False

if password.lower() != password:
    checker["has_upper"] = True
else:
    checker["has_upper"] = False



if all(checker.values()):
    print("This is a BUILT password")
else:
    print("Have 8 characters, an uppercase letter, and a digit to make a stronger password")
