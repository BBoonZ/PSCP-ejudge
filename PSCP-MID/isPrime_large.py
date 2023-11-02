"""isprime_small"""
def main():
    """KKWL"""
    val = int(input())
    prime = True

    if val == 0 or val == 1:
        prime = False

    for i in range(2, int(val**0.5)+1):
        if val%i == 0:
            prime = False
            break

    if prime:
        print('YES')
    else:
        print('NO')
main()
