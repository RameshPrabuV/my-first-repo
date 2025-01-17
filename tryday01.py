
a = float(input("Enter value a:"))

operator = input("Enter operator:")

b = float(input("Enter value b:"))


def addition(a,b):
    sum = a + b
    return sum
def subtraction(a,b):
    sub = a - b
    return sub
def  multiply(a,b):
    mul = a * b
    return mul
def divide(a,b):
    quo = a / b
    if b == 0:
        return "This is error value"
    return quo
def div_rem(a,b):
    rem = a % b
    if b == 0:
        return "This is error value"
    return rem

if operator == "+":
    print(addition(a,b))
elif operator == "-":
    print(subtraction(a,b))
elif operator == "*":
    print(multiply(a,b))
elif operator == "/":
    print(divide(a,b))
elif operator == "%":
    print(div_rem(a,b))
else:
    print("error")
