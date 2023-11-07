"""Resistor"""
def main(color_1, color_2, color_3, color_4):
    """Resisterrrrorror"""
    color = {
        'Black' : [0, 1],
        'Brown' : [1, 10, 1/100],
        'Red' : [2, 100, 2/100],
        'Orange' : [3, 1000],
        'Yellow' : [4, 10000],
        'Green' : [5, 100000, 0.5/100],
        'Blue' : [6, 1000000, 0.25/100],
        'Purple' : [7, 10000000, 0.10/100],
        'Grey' : [8, 100000000, 0.05/100],
        'White' : [9, 1000000000],
        'Gold' : [0, 0.1, 5/100],
        'Silver' : [0, 0.01, 10/100],
    }
    if color_1 not in "Black Brown Red Orange Yellow Green Blue Purple Grey White":
        return print('Error')
    if color_2 not in "Black Brown Red Orange Yellow Green Blue Purple Grey White":
        return print('Error')
    if color_3 not in "Black Brown Red Orange Yellow Green Blue Purple Gold Silver":
        return print('Error')
    if color_4 not in "Brown Red Green Blue Purple Grey Gold Silver":
        return print('Error')

    ohm = int(str(color[color_1][0]) + str(color[color_2][0])) * color[color_3][1]
    omh_2 = ohm*color[color_4][2]
    print("%.4f\n%.4f" %((ohm-omh_2), (ohm+omh_2)))
main(input(), input(), input(), input())
