def rate_performance(score):
    if score > 80:
        return "Distinction"
    elif 60 <= score <= 70:
        return "Credit"
    elif 40 <= score <= 50:
        return "Fair"
    else:
        return "Fail"

def calculator():
    print("Welcome to Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", num1 + num2)
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", num1 * num2)
    elif choice == '4':
        if num2 == 0:
            print("Cannot divide by zero!")
        else:
            print("Result:", num1 / num2)
    else:
        print("Invalid input")

def main():
    score = float(input("Enter student's score: "))
    print("Performance:", rate_performance(score))
    
    calculator()

if __name__ == "__main__":
    main()
