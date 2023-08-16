"""ChristmasTree"""
def christmas():
    """ I REALLY WANT TO STAY AT YOUR HOUSE"""
    val_n = int(input())
    val_k = int(input())
    star = 1
    for i in range(1, val_n+1):
        print(" "*(val_n-i), end='')
        print("*"*(star), end='')
        star += 2
        print()
    for i in range(val_k):
        print(" "*(val_n-2), end='')
        print("---")
christmas()