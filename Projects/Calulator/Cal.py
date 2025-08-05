"""
Created on Tue Aug  5 18:09:47 2025

@author: Roohangiz
"""
#%% Calculator

# Prompt the user to enter the first number and convert it to a float
Num1 = float(input("Enter First In :"))
# Prompt the user to enter the second number and convert it to a float
Num2 = float(input("Enter Second In :"))
# Prompt the user to enter an operation symbol (+, -, *, /)
Op = input("Enter operation :")
# Print label for the result
print("Output:")

# Perform the operation based on the user's input
if Op == "+":
    print(Num1 + Num2)  # Addition
elif Op == "*":
    print(Num1 * Num2)  # Multiplication
elif Op == "/":
    print(Num1 / Num2)  # Division
elif Op == "-":
    print(Num1 - Num2)  # Subtraction
else:
    print("Operation isnot valid")  # Invalid operation entered
