def distance(x1, y1, x2, y2):
    """
    This function calculates the 
    distance between two points on
    coordinate system
    Input parameters: x1, y1, x2, y2
    Output: float rounded to 2 digits
    after point
    """

    return round(((x1-x2)**2 + (y1-y2)**2)**0.5, 2)