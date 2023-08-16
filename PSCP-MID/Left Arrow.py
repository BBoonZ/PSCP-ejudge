"""Left Arrow"""
def main():
    """Shall we talk about it, you called me a friend"""
    val_k = int(input())
    val_n = int(input())
    for i in range(val_n//2, 0, -1):
        print(" "*i, end='')
        print("*"*val_k, end='')
        print()
    for i in range(val_n//2+1):
        print(" "*i, end='')
        print("*"*val_k, end='')
        print()
main()
