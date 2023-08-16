"""LAB2"""
def main():
    """a"""
    val = float(input())
    if val >= 95 and val <= 100:
        print("A")
    elif val > 100:
        print("ERR")
    elif val >= 90:
        print("B+")
    elif val >= 85:
        print("B")
    elif val >= 80:
        print("C+")
    elif val >= 75:
        print("C")
    elif val >= 70:
        print("D+")
    elif val >= 65:
        print("D")
    elif val >= 60:
        print("F+")
    elif val >= 0:
        print("F")
    else:
        print("ERR")
main()