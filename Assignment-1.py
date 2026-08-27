# Write a Python program that will do:
# Handles invalid input (non-numbers, wrong format).
# Performs basic calculations (addition, subtraction, division, etc.).
# Offers optional hard calculations (exponentiation, modulus, etc.).
# Presents results clearly for both basic and hard calculations (if chosen). 
def main():
    print("--- Simple Python Calculator ---")

    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print("\nAvailable operations: +, -, *, /, ^ (exponent), % (modulus)")
    operation = input("Enter the operation (+, -, *, /, ^, %): ").strip()

    result = None

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result = "Error: Division by zero is undefined."
        else:
            result = num1 / num2
    elif operation == "^":
        result = num1**num2
    elif operation == "%":
        if num2 == 0:
            result = "Error: Modulus by zero is undefined."
        else:
            result = num1 % num2
    else:
        result = "Error: Invalid operation selected."

    print(f"\nResult: {result}")


if __name__ == "__main__":
    main()
