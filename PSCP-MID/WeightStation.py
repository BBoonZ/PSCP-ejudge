"""LAB2"""
def main():
    """Pep8"""
    val_1 = float(input())
    val_2 = float(input())
    val_3 = float(input())
    val_4 = float(input())
    val_5 = val_1*4-(val_2+val_3+val_4)
    if val_2+val_3+val_4+val_5 > 15000:
        print("Overweight")
    elif val_2 <= val_1/2 or val_2 >= val_1*2:
        print("Unbalance")
    elif val_3 <= val_1/2 or val_3 >= val_1*2:
        print("Unbalance")
    elif val_4 <= val_1/2 or val_4 >= val_1*2:
        print("Unbalance")
    elif val_5 <= val_1/2 or val_5 >= val_1*2:
        print("Unbalance")
    else:
        print("Pass %.2f"% val_5)
main()