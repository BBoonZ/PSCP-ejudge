"""Kabata"""
def main():
    rob = int(input())
    kabata = ['k', 'b', 't', 'ka', 'ba', 'ta', 'bak', 'bakk', 'bakka']
    bakka = True
    output = check = ''
    for _ in range(rob):
        baka = input()
        check = ''
        for j in baka:
            check += j
            if len(check) <= 2 and check in kabata:
                if len(check) == 2 and check in kabata:
                    check = ''
                continue
            elif len(check) <= 5 and check in kabata:
                if len(check) < 5 and check in kabata:
                    check = ''
                continue
            print(check)
            bakka = False
        if bakka:
            output += 'yes\n'
        else:
            output += 'no\n'
    print(output)
main()
