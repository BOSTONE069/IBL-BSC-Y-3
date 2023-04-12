def main():
    # Prompt the user for a time
    time_str = input("Please enter a time in 24-hour format (e.g., '7:30'): ")

    # Convert the time to hours as a float
    time_hours = convert(time_str)

    # Check if it's time for breakfast, lunch, or dinner, and output the corresponding message if so
    if time_hours < 11.0:
        print("It's breakfast time!")
    elif time_hours < 14.0:
        print("It's lunch time!")
    elif time_hours < 20.0:
        print("It's dinner time!")


def convert(time):
    """
    Converts a time string in 24-hour format to the corresponding number of hours as a float.
    For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), returns 7.5 (i.e., 7.5 hours).
    """
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60


# Call the main() function to run the program
if __name__ == "__main__":
    main()
