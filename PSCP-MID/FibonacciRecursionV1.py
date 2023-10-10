"""FibonacciRecursionV1"""
def fibo(val):
    """gongon"""
    if val == 0:
        return 0
    elif val == 1:
        return 1
    else:
        return fibo(val-1)+fibo(val-2)

print(fibo(int(input())))
