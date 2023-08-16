"""Sequence N"""
def main():
    """a"""
    val = int(input())
    for i in range(val):
        for j in range(val):
            if i == j or j == 0 or j == val-1:
                print("*", end='')
            else:
                print(" ", end='')
        print()
main()