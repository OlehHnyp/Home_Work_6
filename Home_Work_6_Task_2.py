from math import pi

example_set = {'rectangle', 'triangle', 'circle'}
choice = list(set(input(
    "Hello, I can calculate the square of rectangle, \
triangle and circle. Please enter your choice. \
Separate figures by space:"
).lower().split()))

while len(choice)==0 or not set(choice).issubset(example_set):
    choice = list(set(input(
        "Try again! Don't make mistakes, make the choice:"
        ).lower().split()))

rectangle_square = None
triangle_square = None
circle_square = None


def rectangle():
    """
    This function calculate
    the square of rectangle
    Input parameters:
    Output: None
    """

    while 1:
        try:
            rectangle_lenght = float(input(
                "Insert rectangle lenght:"
                ))
            rectangle_height = float(input(
                "Insert rectangle height:"
                ))
            global rectangle_square
            rectangle_square = round(rectangle_lenght*rectangle_height, 2)
            break
        except ValueError:
            print("Try again!")


def triangle():
    """
    This function calculate the square
    of triangle
    Input parameters:
    Output: None
    """
    while 1:
        try:
            triangle_side = float(input(
                "Insert side of triangle:"
                ))
            triangle_height = float(input(
                "Insert triangle height taken from that side:"
                ))
            global triangle_square
            triangle_square = round(0.5 * triangle_side * triangle_height, 2)
            break
        except ValueError:
            print("Try again!")


def circle():
    """
    This function calculate the square
    of circle
    Input parameters:
    Output: None
    """

    while 1:
        try:
            circle_radius = float(input(
                "Enter circle radius:"
                ))
            global circle_square
            circle_square = round(pi * circle_radius**2, 2)
            break
        except ValueError:
            print("Try again!")


for el in choice:
    eval(f"{el}()")

names_and_squares = {'rectangle': rectangle_square,
                     'triangle': triangle_square,
                     'circle': circle_square
                     }

if len(choice) == 1:
    print("The", end=' ')
else:
    print("Here are square:")

for el in choice:
    print(f"{el} square = {names_and_squares.get(el)}")


