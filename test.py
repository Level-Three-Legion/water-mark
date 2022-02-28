def subtract(num1,num2):
	answer = num1 - num2
	return answer
def add(num1,num2):
	answer = num1 + num2
	return answer
def divide(num1,num2):
	answer = num1 / num2
	return answer
def multiply(num1,num2):
	answer = (num1*num2)
	return answer
first = int(input("Enter your first number: "))
second = int(input("Enter your second number: "))
print("""Choose an option:\n(1) Add\n(2) Subtract\n(3) Divide\n(4)Multiply\nChoose a number from the list
""")
choice= int(input("1-4: "))
if choice == 1:
	answer = add(first,second)
elif choice ==2:
	answer = subtract(first,second)
elif choice ==3:
	answer = divide(first,second)
elif choice ==4:
	answer = multiply(first,second)
else:
	print("Choose a number from the list 1-4")
print("The answer is",answer)
