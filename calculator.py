def calculator():
	first_number = float(input("Enter a number:"))
	operator = input("Enter an operator (+, -, *, /): ")
	second_number = float(input("Enter a second number:"))

	if operator == "+":
		result = first_number + second_number
	elif operator == "-":
		result = first_number - second_number
	elif operator == "*":
		result = first_number * second_number
	elif operator == "/":
		if second_number == 0:
			print("Cant divide by 0...")
			return
		result = first_number / second_number
	else:
		print("Invalid operator...")
		return

	print(f"Result: {result}")

calculator()