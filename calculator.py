"""
Simple Calculator Module
Provides basic arithmetic operations: addition, subtraction, multiplication, and division.
"""

class Calculator:
    """A simple calculator class with basic arithmetic operations."""
    
    def add(self, a, b):
        """Add two numbers."""
        return a + b
    
    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b
    
    def divide(self, a, b):
        """Divide a by b. Raises ValueError if b is zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b
    
    def power(self, a, b):
        """Raise a to the power of b."""
        return a ** b
    
    def modulo(self, a, b):
        """Return the remainder of a divided by b."""
        if b == 0:
            raise ValueError("Cannot perform modulo with zero!")
        return a % b


def main():
    """Interactive calculator CLI."""
    calc = Calculator()
    
    print("=" * 50)
    print("Welcome to Python Calculator!")
    print("=" * 50)
    print("\nAvailable operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Modulo (%)")
    print("7. Exit")
    print("=" * 50)
    
    while True:
        try:
            choice = input("\nSelect operation (1-7): ").strip()
            
            if choice == '7':
                print("Thank you for using Python Calculator. Goodbye!")
                break
            
            if choice not in ['1', '2', '3', '4', '5', '6']:
                print("Invalid choice! Please select 1-7.")
                continue
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                result = calc.add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            elif choice == '2':
                result = calc.subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            elif choice == '3':
                result = calc.multiply(num1, num2)
                print(f"\n{num1} × {num2} = {result}")
            elif choice == '4':
                result = calc.divide(num1, num2)
                print(f"\n{num1} ÷ {num2} = {result}")
            elif choice == '5':
                result = calc.power(num1, num2)
                print(f"\n{num1} ^ {num2} = {result}")
            elif choice == '6':
                result = calc.modulo(num1, num2)
                print(f"\n{num1} % {num2} = {result}")
                
        except ValueError as e:
            print(f"\nError: {e}")
        except Exception as e:
            print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
