def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        print("Zero Division Error")
        return None
    return a/b

def calculate(num1,op,num2):
    if op =='+':
        return add(num1,num2)
    elif op =='-':
        return subtract(num1,num2)
    elif op =='*':
        return multiply(num1,num2)
    elif op =='/':
        return divide(num1,num2)
    else:
        print("Invalid operator")
        return None


print("Simple Calculator")
print("--------------------")

while True:
    print("\nMenu:")
    print("1. Calculate")
    print("2. Clear")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")

    if choice =='1':
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            result = calculate(num1,op,num2)

            if result is not None:
                print("Result:",result)

        except ValueError:
            print("Invalid input! Please enter numbers only")

    elif choice =='2':
        print("Screen cleared!")

    elif choice =='3':
        print("Goodbye!")
        break

    else:
        print("Invalid! Try again")