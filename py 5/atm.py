# Solution
# Taking total amount as input from user
Amount = int(input("Please Enter Amount for withdraw : "))

# Calculating the number of notes of different denominations
note_1 = (Amount // 100)  # Number of 100 rupee notes
note_2 = ((Amount % 100) // 50)  # Number of 50 rupee notes
note_3 = ((Amount % 50) // 10)   # Number of 10 rupee notes

# Displaying the results
print("notes of 100 rupee", note_1)
print("notes of 50 rupee", note_2)
print("notes of 10 rupee", note_3)