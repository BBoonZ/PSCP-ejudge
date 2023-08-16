"""Right Arrow"""
def main():
    """Shall we talk about it, you called me a friend"""
    val_k = int(input())
    val_n = int(input())
    for i in range(val_n):
        if i < val_n/2:
            print(" "*i, end='')
        else:
            for _ in range(i+1, val_n):
                print(" ", end='')
        print("*"*val_k, end='')
        print()
main()