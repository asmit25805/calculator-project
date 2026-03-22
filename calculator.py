def get_number(prompt):
    """
    Prompt the user for a number and handle invalid text inputs.
    Loops until a valid number is provided.
    """
    while True:
        user_input = input(prompt).strip()
        try:
            # Try to convert the input to a float (decimal number)
            value = float(user_input)
            
            # If it's a whole number, convert it to an integer for cleaner output
            if value.is_integer():
                return int(value)
            return value
            
        except ValueError:
            # This block catches errors if the user types letters or symbols
            print("❌ Invalid input! Please enter a valid numerical value.")

def get_operator():
    """
    Prompt the user for a mathematical operator.
    Loops until a valid operator is provided.
    """
    valid_operators = ['+', '-', '*', '/']
    while True:
        op = input("Enter operator (+, -, *, /): ").strip()
        if op in valid_operators:
            return op
        print("❌ Invalid operator! Please choose exactly one of: +, -, *, /")

def smart_calculator():
    """Main function to run the interactive calculator loop."""
    print("=" * 30)
    print("🤖 Welcome to the Smart Calculator")
    print("=" * 30)

    while True:
        print("\n--- New Calculation ---")
        
        # 1. Get first number
        num1 = get_number("Enter the first number: ")
        
        # 2. Get operator
        operator = get_operator()
        
        # 3. Get second number
        num2 = get_number("Enter the second number: ")

        result = None

        # 4. Perform the calculation based on the operator
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            # Handle the specific invalid case of dividing by zero
            if num2 == 0:
                print("\n🚨 Error: Division by zero is mathematically impossible!")
            else:
                result = num1 / num2

        # 5. Display the result if no errors occurred
        if result is not None:
            # Format to remove decimal if it's a whole number (e.g., 5.0 -> 5)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
                
            print("-" * 30)
            print(f"✅ Result: {num1} {operator} {num2} = {result}")
            print("-" * 30)

        # 6. Ask to continue or exit
        cont = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if cont not in ['yes', 'y']:
            print("\nThank you for using the Smart Calculator. Goodbye! 👋")
            break

# Standard boilerplate to call the main function
if __name__ == "__main__":
    smart_calculator()
