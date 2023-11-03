"""MultiplyMatrixPQR"""
def main(val_p, val_q, val_r):
  """i love kmitl"""
  matrix_a = [int(input()) for _ in range(val_p*val_q)]
  matrix_b = [int(input()) for _ in range(val_q*val_r)]
  matrix_b2 = []
  for i in range(len(matrix_a)//val_q):
    for j in range(len(matrix_b)):
      if j%val_r == i%val_r:
        matrix_b2.append(matrix_b[j])
  print(matrix_a, matrix_b2)
  total = 0
  for i in range(val_p*val_r):
    for j in range(len(matrix_a)//2):
      print(matrix_a[j], 'for j')
    print('new')
main(int(input()), int(input()), int(input()))
