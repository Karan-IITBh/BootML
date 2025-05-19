class Calculator:                   #Used "class" as per the ques given in discord
    def add(self, a, b):            #Used "func" as per the ques given in discord
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, a, b):
        return a ** b
    
    def modulus(self, a, b):
        if b == 0:
            raise ValueError("Cannot compute modulus with zero")
        return a % b


print("Welcome to the Calculator!")
calc = Calculator()
    
while True:

    print("\nCalculator Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")
    user_input = input("Choose operation (1-7): ")
        
    if user_input == "7":
        print("Exiting...\n")
        break
            
    if user_input in ["1", "2", "3", "4", "5", "6"]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if user_input == "1":
            print(f"Result: {calc.add(a, b)}")
        elif user_input == "2":
            print(f"Result: {calc.subtract(a, b)}")
        elif user_input == "3":
            print(f"Result: {calc.multiply(a, b)}")
        elif user_input == "4":
            print(f"Result: {calc.divide(a, b)}")
        elif user_input == "5":
            print(f"Result: {calc.power(a, b)}")
        elif user_input == "6":
            print(f"Result: {calc.modulus(a, b)}")
    else:
        print("Invalid operation")

