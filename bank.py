# Prompt the user for a greeting
greeting = input("Please enter a greeting: ")

# Convert the greeting to lowercase and remove any leading whitespace
greeting = greeting.strip().lower()

# Check the first letter of the greeting and output the appropriate amount
if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
