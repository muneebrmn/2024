# Coded By Muneeb Ur Rehman
# A Simple Calculator Capable Of Addition, Subtraction, Multiplication & Division Between Two Numbers.

num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))
Operator = input("Enter an operator: ")

if Operator == "+":
  print(num_1 + num_2)
elif Operator == "-":
  print(num_1 - num_2)
elif Operator == "*":
  print(num_1 * num_2)
elif Operator == "/":
  print(num_1 / num_2)
else:
  print("Please Input A Valid Operator And Try Again.")

# Thank You For Using This Calculator!  
