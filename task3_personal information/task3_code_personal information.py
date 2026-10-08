name = input("Enter your name: ").strip()
age_text = input("Enter your age: ").strip()
city = input("Enter your city: ").strip()

try:
    age = int(age_text)
except ValueError:
    print("Please enter your age as a whole number.")
else:
    print("\n--- Personal Information ---")
    print(f"Hello! My name is {name}.")
    print(f"I am {age} years old.")
    print(f"I am from {city}.")
