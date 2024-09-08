import math

def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    area = math.pi * (radius ** 2)
    return area

# Get user input for the radius
try:
    radius = float(input("Enter the radius of the circle: "))
    if radius < 0:
        print("Radius cannot be negative. Please enter a valid radius.")
    else:
        area = calculate_circle_area(radius)
        print(f"The area of the circle with radius {radius} is {area:.2f}")
except ValueError:
    print("Invalid input. Please enter a numeric value for the radius.")
