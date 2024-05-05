# import math module for options 5 & 6
import math
# establish baseline for variables that will be altered throughout the loop
total_rounds = 0
total_value = 0
result = float(0)
user_selection = 1
menu = True
# use 1st while loop to display menu
while menu == True:
    print(f"Current Result: {result}")
    print()
    print("Calculator Menu")
    print("-" * 15)
    print("0. Exit Program")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Logarithm")
    print("7. Display Average")
    # use 2nd while loop to ask for user input for options 0-7
    while user_selection in range(0, 8):
        menu_selection = int(input("Enter Menu Selection: "))
        if total_rounds == 0 and menu_selection == 7:
            print("Error: No calculations yet to average!")
        # for EC use RESULT to store previous round's result
        elif (menu_selection > 0 and menu_selection < 7):
            operand_a = input("Enter first operand: ")
            if operand_a == "RESULT":
                first_num = float(result)
            else:
                first_num = float(operand_a)
            operand_b = input("Enter second operand: ")
            if operand_b == "RESULT":
                second_num = float(result)
            else:
                second_num = float(operand_b)
            print()
            # perform operations with both user inputs
            if menu_selection == 1:
                result = first_num + second_num
                total_rounds += 1
                total_value += result
                break
            elif menu_selection == 2:
                result = first_num - second_num
                total_rounds += 1
                total_value += result
                break
            elif menu_selection == 3:
                result = first_num * second_num
                total_rounds += 1
                total_value += result
                break
            elif menu_selection == 4:
                result = first_num / second_num
                total_rounds += 1
                total_value += result
                break
            elif menu_selection == 5:
                result = math.pow(first_num, second_num)
                total_rounds += 1
                total_value += result
                break
            elif menu_selection == 6:
                result = math.log(second_num, first_num)
                total_rounds += 1
                total_value += result
                break
            print(f"Current Result: {result}")
            total_rounds += 1
            total_value += result
        # use option 7 to provide statistics of previous calculations
        elif menu_selection == 7:
            print(f"Sum of calculations: {total_value}")
            print(f"Number of calculations: {total_rounds}")
            print(f"Average of calculations: {float(total_value / total_rounds):.2f}")
        elif menu_selection == 0:
            print("Thanks for using this calculator. Goodbye!")
            exit()
        else:
            print("Error: Invalid selection!")

