"""All_Primes"""
def main():
    """KKWL"""
    val = int(input())
    count = 0
    for i in range(1, val+1):
        prime = True

        if i == 0 or i == 1:
            prime = False

        for j in range(2, i):
            if i%j == 0:
                prime = False
                break

        if prime:
            count += 1
    print(count)
main()
