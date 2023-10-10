"""Binary"""
def main():
    """binaryyyyy"""
    val = int(input())
    output = ''
    if val == 0:
        return print(0)
    while val > 0:
        output += str(val%2)
        val //= 2
    print(output[-1::-1])
main()
