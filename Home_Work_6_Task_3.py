def calculate_characters():
    """
    This function calculate the number
    of characters included in a given
    string
    Input parameters:
    Output: print numbers and characters
    """

    string = input("Enter a frase which you want to count:")

    for char in set(string):
        print(f"{char} = {string.count(char)}")


calculate_characters()