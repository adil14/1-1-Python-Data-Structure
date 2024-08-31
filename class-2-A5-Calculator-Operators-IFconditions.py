

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
operator = str(input("Enter Operator : "))
if operator == "+":
    result = num1 + num2
if operator == "-":
    result == num1 - num2
if operator == "*":
    result = num1 * num2
if operator == "/":
    result == num1 + num2
print("Result is : ", result)


num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
operator = str(input("Enter Operator : "))
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result == num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result == num1 / num2
else:
    print("Enter numbers only")
print("Result is : ", result)

marks = int(input("Enter total marks : "))
if marks > 90:
    print("you got A grade")
if marks < 60:
    print("you are fail") 