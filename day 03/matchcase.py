print("""
        Add +
        Sub -
        Mul *
        Div /
""")

num1 = float(input("Enter num 1: "))
num2 = float(input("Enter num 2: "))
ch = input("Enter your choice: ")

match ch:
    case "+":
        print(num1 + num2)

    case "-":
        print(num1 - num2)

    case "*":
        print(num1 * num2)

    case "/":
        print(num1 / num2)

    case _:
        print("Invalid choice")