"""Sequence II"""
def main():
    """w"""
    val = int(input())
    for i in range(0, val):
        if i % 7 == 0 and  i != 0:
            print()
        print(val-i, end=' ')
main()