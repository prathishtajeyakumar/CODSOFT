num1 = int(input("Enter number 1: "))
op = input("Enter the operation: ")
num2 = int(input("Enter number 2: "))

match op:
  case "+":
    print(num1 + num2)
  case "-":
    print(num1 - num2)

  case "*":
    print(num1 * num2)

  case "/":
    print(num1 / num2)

  case "%":
    print(num1 % num2)