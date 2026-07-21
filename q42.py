password = "python123"
attempts = 3

while attempts > 0:
    user = input("Enter password: ")

    if user == password:
        print("Access granted")
        break
    else:
        attempts -= 1
        print("Wrong password")

if attempts == 0:
    print("Access denied")