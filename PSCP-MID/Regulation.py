"""DAY1"""
def main(val_x, val_y, val_z):
    """A"""
    print("%30d" %val_x)
    print("%030d" %val_x)
    print("%.2f" %val_y)
    print("%.12f" %val_y)
    print("%40s" %val_z)
main(int(input()), float(input()), str(input()))