"""Sequence VII"""
def main():
    """w"""
    val = int(input())
    for i in range(1, val*2):
        if i <= val:
            for j in range(0, i):
                print(j+1, end=' ')
            print()
        else:
            for j in range(1, val*2-i+1):
                print(j, end=' ')
            print()
main()