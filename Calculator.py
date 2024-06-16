# Coded By Muneeb Ur Rehman
# A Simple Calculator Capable Of Addition, Subtraction, Multiplication & Division Between Two Numbers.

Num1 = int(input("Enter a number: "))
Num2 = int(input("Enter a number: "))
Operator = input("Enter an operator: ")

if Operator == "+":
  print(Num1 + Num2)
elif Operator == "-":
  print(Num1 - Num2)
elif Operator == "*":
  print(Num1 * Num2)
elif Operator == "/":
  print(Num1 / Num2)
else:
  print("Please Input A Valid Operator And Try Again.")

# Thank You For Using This Calculator!  