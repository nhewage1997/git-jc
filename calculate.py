
def calculate_area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    import math
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2

def calculate_area_of_rectangle(length, width):
    """Calculate the area of a rectangle given its length and width."""
    if length < 0 or width < 0:
        raise ValueError("Length and width cannot be negative.")
    return length * width

def calculate_area_of_octagon(side_length):
    """Calculate the area of a regular octagon given the length of its sides."""
    if side_length < 0:
        raise ValueError("Side length cannot be negative.")
    return 2 * (1 + 2**0.5) * side_length ** 2