num = input("enter a number")

if len(num) >= 4:
    mid = len(num) // 2
    product = int(num[mid-1]) * int(num[mid])
    print("product of the two numbers are: ", product)
else:
    print("numbers must be more than or equal to four digits")