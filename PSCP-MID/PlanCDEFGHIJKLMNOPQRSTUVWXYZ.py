"""LAB2"""
def main():
    """a"""
    txt = input()
    val1 = float(input())
    val2 = float(input())
    val3 = float(input())
    if txt == 'Ascend':
        if val1 >= val2 and val3 >= val2:
            if val1 >= val3:
                print("%.2f, %.2f, %.2f"% (val2, val3, val1))
            elif val1 <= val3:
                print("%.2f, %.2f, %.2f"% (val2, val1, val3))
        elif val2 >= val1 and val3 >= val1:
            if val2 >= val3:
                print("%.2f, %.2f, %.2f"% (val1, val3, val2))
            elif val2 <= val3:
                print("%.2f, %.2f, %.2f"% (val1, val2, val3))
        elif val3 <= val1 and val3 <= val2:
            if val1 >= val2:
                print("%.2f, %.2f, %.2f"% (val3, val2, val1))
            elif val2 >= val1:
                print("%.2f, %.2f, %.2f"% (val3, val1, val2))
    if txt == 'Descend':
        txt2(val1, val2, val3)
 
def txt2(val1, val2, val3):
    """w"""
    if val1 <= val2 and val3 <= val2:
        if val1 <= val3:
            print("%.2f, %.2f, %.2f"% (val2, val3, val1))
        elif val1 >= val3:
            print("%.2f, %.2f, %.2f"% (val2, val1, val3))
    elif val2 <= val1 and val3 <= val1:
        if val2 <= val3:
            print("%.2f, %.2f, %.2f"% (val1, val3, val2))
        elif val2 >= val3:
            print("%.2f, %.2f, %.2f"% (val1, val2, val3))
    elif val3 >= val1 and val3 >= val2:
        if val1 <= val2:
            print("%.2f, %.2f, %.2f"% (val3, val2, val1))
        elif val2 <= val1:
            print("%.2f, %.2f, %.2f"% (val3, val1, val2))
main()