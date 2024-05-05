new_password = ''

print("Menu")
print("-" * 12)
print("1. Encode")
print("2. Decode")
print("3. Quit")
print()
user_option = int(input("Please enter an option: "))

menu_option = True

while menu_option:
    password = input("Please enter your password to encode: ")
    if user_option == 1:
        for n in range(0, len(password)):
            x = int(password[n]) + 3
            new_password += str(x)

    print(new_password)
