"""Matrix_MN"""
def main():
    """magidccc"""
    val_m = int(input())
    val_n = int(input())
    num = []
    for i in range(val_m*val_n):
        num.append(int(input()))

    for i in range(val_m):
        for j in range(i*val_n, (i+1)*val_n):
            print(num[j], end=' ')
        print()
main()
