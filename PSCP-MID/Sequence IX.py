"""Sequence VII"""
def main():
    """w"""
    val = int(input())
    for i in range(1, val+1):
        for _ in range(val-i):
            print("  ", end=' ')
        for j in range(i):
            print("%02d"% (j+1), end=' ')
        for j in range(i-1, 0, -1):
            print("%02d"% j, end=' ')
        print()
main()