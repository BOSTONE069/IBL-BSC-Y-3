# Prompt the user for the answer to the Great Question of Life, the Universe and Everything
answer = input(
    "What is the answer to the Great Question of Life, the Universe and Everything? ")

# Convert the answer to lowercase for case-insensitive comparison
if answer.lower() in ["42", "forty-two", "forty two"]:
    # If the answer is 42, "forty-two", or "forty two", print "Yes"
    print("Yes")
else:
    # Otherwise, print "No"
    print("No")
