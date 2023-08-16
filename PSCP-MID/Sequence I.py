"""Sequence I"""
def main():
    """w"""
    val = int(input())
    for _ in range(1, val+1):
        for j in range(1, val+1):
            print(j, end=' ')
        print()
main()