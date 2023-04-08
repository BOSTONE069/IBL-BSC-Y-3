while True:
    try:
        x = int(input("Enter the value of x? "))
        print(f"x is {x}")
    except ValueError:
        print("X is not an integer")
    else:
        break

print(f"x is {x}")
