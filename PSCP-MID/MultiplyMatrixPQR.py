"""MultiplyMatrixPQR"""
def main(val_p, val_q, val_r):
    """i love kmitl"""
    matrix_a = [[int(input()) for _ in range(val_q)] for _ in range(val_p)]
    matrix_b = [[int(input()) for _ in range(val_r)] for _ in range(val_q)]
    output = []
    total = count = 0
    for i in range(len(matrix_a)):
        for j in range(val_r):
            for k in range(len(matrix_a[i])):
                total += matrix_a[i][k]*matrix_b[k][j]
                count += 1
                if count%val_q == 0:
                    output.append(total)
                    total = 0
    for i in range(len(output)):
        if i%val_r == 0 and i != 0:
            print()
        print(output[i], end=' ')
main(int(input()), int(input()), int(input()))
