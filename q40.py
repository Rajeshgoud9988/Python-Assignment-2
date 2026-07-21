print("Welcome to the Grade Checker Program!")

while True:
    marks = float(input("Enter your marks (0-100): "))

    if 90 <= marks <= 100:
        print("Your grade is A+")
    elif 80 <= marks < 90:
        print("Your grade is A")
    elif 70 <= marks < 80:
        print("Your grade is B")
    elif 60 <= marks < 70:
        print("Your grade is C")
    elif 50 <= marks < 60:
        print("Your grade is D")
    else:
        print("Your grade is Fail")

    choice = input("Do you want to continue? (yes/no): ").lower()

    if choice == "no":
        print("Thank you")
        break