# Solution

actual_cost = float(input("Please Enter the Actual Product Price: "))
sale_amount = float(input("Please Enter the Sales Amount: "))

if (sale_amount > actual_cost):
    profit = sale_amount - actual_cost
    print("Total Profit = {0}".format(profit))
else:
    print("No Profit!!!")