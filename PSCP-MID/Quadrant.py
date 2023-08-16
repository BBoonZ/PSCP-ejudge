"""LAB2"""
def main():
    """a"""
    val_x = int(input())
    val_y = int(input())
    if val_x == 0 and val_y == 0:
        print("O")
    elif val_x != 0 and val_y == 0:
        print("X")
    elif val_y != 0 and val_x == 0:
        print("Y")
    elif val_x > 0 and val_y > 0:
        print("Q1")
    elif val_x > 0 and val_y < 0:
        print("Q4")
    elif val_x < 0 and val_y > 0:
        print("Q2")
    elif val_x < 0 and val_y < 0:
        print("Q3")
main()