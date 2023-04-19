with open("name.txt", "r") as file:
    for line in file:
        print("Hello, ", line.rstrip())