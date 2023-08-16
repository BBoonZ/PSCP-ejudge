"""Sequence II"""
def main():
    """w"""
    val = int(input())
    for i in range(0, val):
        for j in range(val*i+1, val+val*i+1):
            print(j, end=' ')
        print()
main()