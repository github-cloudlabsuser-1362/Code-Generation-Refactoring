# create a basic calculator
# This is a simple calculator program that performs basic arithmetic operations: addition, subtraction, multiplication, and division.
# It prompts the user to enter two numbers and an operator, then performs the corresponding operation and displays the result.      

# The program handles invalid inputs and division by zero errors gracefully.
# It also includes a function to perform the calculation based on the operator provided by the user.
# The calculator supports the following operations: 
# addition (+), subtraction (-), multiplication (*), and division (/).
# The program continues to prompt the user for input until they choose to exit by entering 'q'.
# The calculator is designed to be user-friendly and provides clear instructions for usage.
# The calculator is implemented in Python and can be run in any Python environment.

# start by having a basic loop that accepts user input and parses the text, then does the calculation and outputs th eresult

def calculator():
    print("Welcome to the basic calculator!")
    print("You can perform the following operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("Type 'q' to quit the calculator.")
    
    while True:
        user_input = input("\nEnter your calculation (e.g., 2 + 2): ")
        
        if user_input.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break
        
        try:
            # Split the input into components
            num1, operator, num2 = user_input.split()
            num1 = float(num1)
            num2 = float(num2)
            
            # Perform the calculation based on the operator
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = num1 / num2
            else:
                raise ValueError("Invalid operator. Please use +, -, *, or /.")
            
            print(f"Result: {result}")
        
        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    calculator()