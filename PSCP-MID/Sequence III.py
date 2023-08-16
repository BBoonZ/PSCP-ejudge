"""Sequence II"""
def main():
    """w"""
    val = int(input())
    for i in range(2, val+2):
        for j in range(i, val+i):
            print(j, end=' ')
        print()
main()