"""Colors"""
def main(color_1, color_2):
    """Color!S"""
    if (color_1 == 'Red' and color_2 == 'Yellow') or (color_2 == 'Red' and color_1 == 'Yellow'):
        print('Orange')
    elif (color_1 == 'Yellow' and color_2 == 'Blue') or (color_2 == 'Yellow' and color_1 == 'Blue'):
        print('Green')
    elif (color_1 == 'Red' and color_2 == 'Blue') or (color_2 == 'Red' and color_1 == 'Blue'):
        print('Violet')
    elif color_1 == color_2 and (color_1 in ['Blue', 'Yellow', 'Red']):
        print(color_1)
    else:
        print('Error')
main(input(), input())
