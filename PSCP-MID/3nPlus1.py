"""3nPlus1"""
def main():
    """งาวง"""
    output = ''
    while True:
        val = int(input())
        count = 1
        if val == 0:
            break
        while True:
            if val%2 != 0:
                val *= 3
                val += 1
            elif val%2 == 0:
                val //= 2

            count += 1
            if val == 1:
                break
        output += str(count) + '\n'
    print(output)
main()
