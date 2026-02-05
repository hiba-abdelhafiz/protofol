correct_password = "12345"
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    password = input("Enter password: ")
    if password == correct_password:
        print("Password correct! Access granted.")
        break
    else:
        attempts += 1
        print(f"Wrong password. {max_attempts - attempts} attempts left.")
else:
    print("Maximum attempts reached. Authorities alerted!")
