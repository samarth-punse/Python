# A scientist wants to find out how much different items would weigh on the moon.
# They have written a program which allows you to enter the mass of an object in kg and it will tell you how
# much that object will weigh both on Earth and on the Moon.
# The weight of an object is calculated using the following formula:
# weight = mass × gravitational field strength
# Using the file ‘Q01 challenge 1’ gravity below:
# Amend the lines at the bottom of the code to give the:
# * identifier of a constant used in the code
# * name of a user-defined function
# * data type of the layout variable
# * name of a parameter used in the code
# * arithmetic operator used in the code

EARTH_GRAVITY = 9.81
MOON_GRAVITY = 1.62

def calculate_weight(mass, gravity):
    return mass * gravity

def main():
    # User input
    mass = float(input("Enter the mass of the object in kg: "))

    weight_earth = calculate_weight(mass, EARTH_GRAVITY)
    weight_moon = calculate_weight(mass, MOON_GRAVITY)

    layout = f"An object with a mass of {mass} kg weighs:\n- {weight_earth:.2f} N on Earth\n- {weight_moon:.2f} N on the Moon"

    print("\n" + layout)


if __name__ == "__main__":
    main()


# =========================================================
# Q01 challenge 1 Answers
# =========================================================
# Identifier of a constant used in the code: EARTH_GRAVITY
# Name of a user-defined function: calculate_weight
# Data type of the layout variable: String (str)
# Name of a parameter used in the code: mass
# Arithmetic operator used in the code: *
