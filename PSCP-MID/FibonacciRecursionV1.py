"""FibonacciRecursionV1"""
def fibo(val):
    if val == 0:
        return 0
    if val == 1:
        return 1
    else:
        return fibo(val-1)+fibo(val-2)
fibo(int(input()))
