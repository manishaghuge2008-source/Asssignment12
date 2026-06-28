import math
import random
from datetime import datetime


history = {}

# Basic arithmetic functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero!"

# Main program
try:
    while True:
        print("\n===== SMART CALCULATOR MENU =====")
        print("1. Basic Arithmetic")
        print("2. Scientific Calculation")
        print("3. Generate Random Number")
        print("4. View History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        # 1. Basic Arithmetic
        if choice == "1":
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                print("1.Add  2.Subtract  3.Multiply  4.Divide")
                op = input("Choose operation: ")

                if op == "1":
                    result = add(a, b)
                    print("Result:", result)

                elif op == "2":
                    result = subtract(a, b)
                    print("Result:", result)

                elif op == "3":
                    result = multiply(a, b)
                    print("Result:", result)

                elif op == "4":
                    result = divide(a, b)
                    print("Result:", result)

                else:
                    print("Invalid operation!")

                # Store in history
                time = str(datetime.now())
                history[time] = f"Arithmetic Result: {result}"

            except ValueError:
                print("Invalid input! Enter numbers only.")

        # 2. Scientific Calculations
        elif choice == "2":
            try:
                num = float(input("Enter a number: "))

                print("1.Sqrt  2.Square  3.Sin  4.Cos")
                op = input("Choose operation: ")

                if op == "1":
                    result = math.sqrt(num)

                elif op == "2":
                    result = math.pow(num, 2)

                elif op == "3":
                    result = math.sin(num)

                elif op == "4":
                    result = math.cos(num)

                else:
                    print("Invalid choice!")
                    continue

                print("Result:", result)

                time = str(datetime.now())
                history[time] = f"Scientific Result: {result}"

            except ValueError:
                print("Invalid input!")

        # 3. Random Number
        elif choice == "3":
            rand_num = random.randint(1, 100)
            print("Random Number:", rand_num)

            time = str(datetime.now())
            history[time] = f"Random Number: {rand_num}"

        # 4. View History
        elif choice == "4":
            if not history:
                print("No history available!")
            else:
                print("\n----- HISTORY -----")
                for time, result in history.items():
                    print(time, "=>", result)

        # 5. Exit
        elif choice == "5":
            print("Exiting program... Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1-5.")

except Exception as e:
    print("Error occurred:", e)