"""Diginity"""
def main():
    """TMD is BEST"""
    output = ''
    while True:
        num = input()
        if num == '0':
            break
        while True:
            check = 0
            if len(num) == 1:
                break
            for i in num:
                check += int(i)
            num = str(check)
        output += num + '\n'
    print(output)
main()
