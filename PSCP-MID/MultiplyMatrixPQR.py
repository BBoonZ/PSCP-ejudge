"""MultiplyMatrixPQR"""
def main(val_p, val_q, val_r):
  """i love kmitl"""
  matrix_a = [int(input()) for _ in range(val_p*val_q)]
  matrix_b = [int(input()) for _ in range(val_q*val_r)]
  for i in range(val_p*val_q):
    for j in range(val_r):
        print(matrix_a[i][j])
main(int(input()), int(input()), int(input()))
