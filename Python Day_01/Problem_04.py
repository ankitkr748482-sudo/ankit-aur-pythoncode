#  Made a simple calculator 

num1 = float(input("Enter first number:"))
operator = input(" +,-,*,/,% :")
num2 = float(input("Enter second number:"))

if ( operator == "+"):
    print("Result is:", num1 + num2)
elif( operator == "-"):
    print("Result is:", num1 - num2)
elif( operator == "*"):
    print("result is:", num1 * num2)
elif( operator == "/"):
    print("Result is:", num1 / num2)
elif( operator == "%"):
    print("Result is:", num1 % num2)
else:
    print("Invalid operator")