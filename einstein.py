# Define the speed of light in meters per second
SPEED_OF_LIGHT = 300000000

# Prompt the user for mass in kilograms and store the result in a variable called mass
mass = int(input("Please enter mass in kilograms: "))

# Calculate the equivalent energy in Joules and store the result in a variable called energy
energy = mass * SPEED_OF_LIGHT ** 2

# Output the energy in Joules to the console
print("The equivalent energy is:", energy, "Joules")
