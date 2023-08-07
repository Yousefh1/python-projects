# This is a simple calculator I build After just learning some of the basics

number1 = float(input("Please enter your first number "))
number2 = float(input("Enter your second number that number would like to calculate "))
operations = input("Please enter your chosen operations(+, -, *, /): ")

def add(number1,number2):
    return number1 + number2

def substract(number1,number2):
    return number1 - number2

def multiply(number1,number2):
    return number1 * number2

def divide(number1,number2):
    return number1 / number2

if operations == "+":
      result =  add(number1, number2)
elif operations == "-":
    result =  substract(number1, number2)
elif operations == "/":
    result =  divide(number1, number2)
elif operations == "*":
    result =  multiply(number1, number2)
else:
    "Choose the correct operations sign"


try:
    if operations == "/":
        if number2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        result = number1 / number2
    else:
        raise ValueError("Invalid operation")
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)
else:
    print("Result:", result)
