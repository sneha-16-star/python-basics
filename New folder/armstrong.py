

num = int(input("Enter a Number: "))

n = len(str(num))

sum_of_powers = 0
temp = num

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** n  # Raise to the power of number of digits
    temp //= 10

if num == sum_of_powers:
    print(num, "is an Armstrong Number")
else:
    print(num, "is not an Armstrong Number")