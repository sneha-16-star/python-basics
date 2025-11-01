# Solution

# Take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("Maths: "))
english = int(input("English: "))
science = int(input("Science: "))
hindi = int(input("Hindi: "))

# Let's calculate the percentage of marks
sum_of_math_english_science_hindi = math + english + science + hindi
perc = (sum_of_math_english_science_hindi / 400) * 100

print("Percentage Mark = ", perc)