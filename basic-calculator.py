
# Basic Calculator

number_1 = float(input("Enter a number: "))

operator = input("Enter an operation (+, -, *, /): ")

number_2 = float(input("Enter another number: "))

if operator == "+":
    print(number_1 + number_2)
elif operator == "-":
    print(number_1 - number_2)
elif operator == "*":
    print(number_1 * number_2)
elif operator == "/":
    print(number_1 / number_2)

else:
    print("Invalid Entry")
