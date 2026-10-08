# Task 5: Mini Python Program
# Age Calculator

print("===== AGE CALCULATOR =====")

# Get birth year and current year from the user
birth_year = int(input("Enter your birth year: "))
current_year = int(input("Enter the current year: "))

# Calculate age
age = current_year - birth_year

# Display the result
print("\n===== RESULT =====")
print("Birth Year:", birth_year)
print("Current Year:", current_year)
print("Your age is:", age, "years")