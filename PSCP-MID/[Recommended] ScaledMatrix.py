"""[Recommended] ScaledMatrix"""
def main(val_m, val_n):
    """the matrix"""
    matrix = [float(input()) for _ in range(val_m*val_n)]
    for i in range(val_m*val_n):
        if i%val_n == 0 and i != 0:
            print()
        print("%.2f" %((matrix[i]-min(matrix))/(max(matrix)-min(matrix))), end=' ')
main(int(input()), int(input()))
