# Super Simple Square Root Program
number = float(input("Enter a number: "))

if number >= 0:
    result = number ** 0.5
    print(f"Square root of {number} = {result}")
else:
    print("Please enter a positive number!")