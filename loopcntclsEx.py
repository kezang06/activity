num = 10

while num >= 1:
    print(num)
    num -= 1

print("Time's up!")

total = 0

while True:
    num = int(input("Enter an integer (0 to stop): "))
    if num == 0:
        break
    total += num

print("Total sum:", total)

correct_username = "admin"
correct_password = "1234"

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        attempts -= 1
        print("Incorrect credentials. Attempts left:", attempts)

if attempts == 0:
    print("Account Locked")