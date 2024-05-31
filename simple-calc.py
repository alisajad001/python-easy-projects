num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

operation = input("Enter the operation (+, -, *, /): ")

result = 0

if operation == "+":
  result += num_1 + num_2
elif operation == "-":
  result += num_1 - num_2
elif operation == "*":
  result += num_1 * num_2
elif operation == "/":
  result += num_1 / num_2
else:
  print("Invalid operation!")

print(f"The result is {result}")