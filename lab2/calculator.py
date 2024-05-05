# Ask user for two inputs
first_operand = float(input("Enter first operand: "))
second_operand = float(input("Enter second operand: "))
print()
#print options for user selection
print("Calculator Menu")
print("---------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print()
#perform operations with user selection
operation = input("Which operation do you want to perform? ")
print()
if operation == "1":
    print("The result of the operation is ", first_operand + second_operand, ". Goodbye!", sep="")
elif operation == "2":
    print("The result of the operation is ", first_operand - second_operand, ". Goodbye!", sep="")
elif operation == "3":
    print("The result of the operation is ", first_operand * second_operand, ". Goodbye!", sep="")
elif operation == "4":
    print("The result of the operation is ", first_operand / second_operand, ". Goodbye!", sep="")
else:
    print("Error: Invalid selection! Terminating program.")
