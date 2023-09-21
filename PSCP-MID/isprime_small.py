"""isprime_small"""
def main():
    """KKWL"""
    val = int(input())
    prime = True

    if val == 0 or val == 1:
        prime = False

    for i in range(2, val):
        if val%i == 0:
            prime = False
            break

    if prime:
        print('Yes')
    else:
        print('No')
main()
