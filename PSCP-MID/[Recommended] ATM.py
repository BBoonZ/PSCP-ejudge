"""[Recommended] ATM"""
def main():
    """money rain no pain no gain"""
    money = int(input())
    while True:
        txt = input()
        if txt == 'END':
            break
        if txt[0] == 'W':
            money -= int(txt.split()[1])
            money = max(money, 0)
        else:
            money += int(txt.split()[1])
    print(money)
main()
