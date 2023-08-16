"""Sequence II"""
def main():
    """w"""
    val = int(input())
    for i in range(1, val+1):
        for j in range(0, i):
            print(j+1, end=' ')
        print()
main()