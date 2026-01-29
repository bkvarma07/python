name = input("Enter your name: ")
email = input("Enter your email: ")
number = input("Enter your mobile number: ")
age = int(input("Enter your age: "))

valid = True

if name[0] == " " or name[len(name) - 1] == " " or name.count(" ") < 1:
    valid = False

if email.count("@") != 1 or "." not in email or email[0] == "@":
    valid = False

if len(number) != 10 or not number.isdigit() or number[0] == "0":
    valid = False

if age < 18 or age > 60:
    valid = False

if valid:
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")