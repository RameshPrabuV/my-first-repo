import sys

def addition(num1,num2):
    add = num1 + num2
    return add

def substract(num1,num2):
    sub = num1 - num2
    return sub

def multiply(num1,num2):
    mul = num1 * num2
    return mul

def divide(num1,num2):
    div = num1 / num2
    if num2 == 0:
        return "This is error."
    return div

def main():
    if len(sys.argv) != 4:
        print("provide this format <num1> <operator> <num2>")
        return

    try:
        num1 = float(sys.argv[1])
        operator = sys.argv[2]
        num2 = float(sys.argv[3])

        if operator == "+":
            output = addition(num1,num2)
            print(output)

        elif operator == "-":
            output = substract(num1,num2)
            print(output)

        elif operator == "*":
            output = multiply(num1,num2)
            print(output)

        elif operator == "/":
            output = divide(num1,num2)
            print(output)
        else:
                print(f"Error: Unsupported operator '{operator}'. Use +, -, *, or /.")
    except ValueError:
        print("Error: Invalid number input. Please provide valid numeric values.")

if __name__ == "__main__":
    main()