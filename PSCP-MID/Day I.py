"""LAB2"""
def main():
    """a"""
    year = int(input())
    if year % 400 == 0:
        print("Yes")
    elif year % 100 == 0:
        print("No")
    elif year % 4 == 0:
        print("Yes")
    else:
        print("No")
main()