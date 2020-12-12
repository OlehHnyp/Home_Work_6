from math import pi

example_set = {'rectancle', 'triancle', 'circle'}

choice = list(set(input(
    "Hello, I can calculate the square of rectangle, \
triangle and circle. Please enter your choice. \
Separate figures by space:"
).lower().split()))

while len(choice)==0 or not set(choice).issubset(example_set):
    choice = list(set(input(
        "Try again! Don't make mistakes, make the choice."
        ).lower().split()))

rectancle_square = None
triancle_square = None
circle_square = None


def rectancle():
    """
    This function calculate
    the square of rectancle
    Input parameters:
    Output: float
    """

    while 1:
        try:
            rectancle_lenght = float(input(
                "Insert rectancle lenght:"
                ))
            rectancle_height = float(input(
                "Insert rectancle height:"
                ))
            global rectancle_square
            rectancle_square = round(rectancle_lenght*rectancle_height, 2)
            break
        except ValueError:
            print("Try again!")


def triancle():
    """
    This function calculate the square
    of triancle
    Input parameters:
    Output: float
    """
    while 1:
        try:
            triancle_side = float(input(
                "Insert side of triancle:"
                ))
            triancle_height = float(input(
                "Insert triancle heigh taken from that side:"
                ))
            global triancle_square
            triancle_square = round(0.5 * triancle_side * triancle_height, 2)
            break
        except ValueError:
            print("Try again!")


def circle():
    """
    This function calculate the square
    of circle
    Input parameters:
    Output: float
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

names_and_squares = {'rectancle': rectancle_square,
                     'triancle': triancle_square,
                     'circle': circle_square
                     }

if len(choice) == 1:
    print("The", end=' ')
else:
    print("Here are square:")

for el in choice:
    print(f"{el} square = {names_and_squares.get(el)}")


