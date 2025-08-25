import math

def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /  sin  cos  tan")
    
    while True:
        operation = input("Enter operation (+, -, *, /, sin, cos, tan or 'exit' to quit): ").strip().lower()
        
        if operation == 'exit':
            print("Goodbye!")
            break
        
        if operation in ['+', '-', '*', '/']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if operation == '+':
                    result = num1 + num2
                elif operation == '-':
                    result = num1 - num2
                elif operation == '*':
                    result = num1 * num2
                elif operation == '/':
                    if num2 == 0:
                        print("Error: Division by zero.")
                        continue
                    result = num1 / num2

                print("Result:", result)
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        
        elif operation in ['sin', 'cos', 'tan']:
            try:
                angle = float(input("Enter angle in degrees: "))
                radians = math.radians(angle)

                if operation == 'sin':
                    result = math.sin(radians)
                elif operation == 'cos':
                    result = math.cos(radians)
                elif operation == 'tan':
                    result = math.tan(radians)

                print(f"{operation}({angle}) = {result}")
            except ValueError:
                print("Invalid input. Please enter a valid angle.")
        
        else:
            print("Invalid operation. Try again.")
        print("Developed by:selamawit G/egziabher")
 
:c







:c
