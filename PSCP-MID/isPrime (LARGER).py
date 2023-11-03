"""isPrime (LARGER)"""
def main():
    """KKWL"""
    val = int(input())
    prime = True

    if val == 0 or val == 1:
        prime = False

    if val%2 == 0:
        pass

    for i in range(3, int(val**0.5)+1, 2):
        if val%i == 0:
            prime = False
            break

    if prime:
        print('True')
    else:
        print('False')
main()
