
age=int(input("Enter your age: "))
nationality=input("Enter your nationality:")
if nationality=='indian':
    if age>=18:
        print("You are eligible to vote")
    else:
        print("You are not eligible to vote age is less than 18")
else:
    print("You are not eligible to vote as you are not an Indian citizen")
