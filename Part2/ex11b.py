def calculate(number1, operator, number2):
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        return number1 / number2
    else:
        return "Invalid operator"
print(calculate(10, "+", 10))
print(calculate(10,"-",10))
print(calculate(10,"*",10))
print(calculate(10,"/",10))
