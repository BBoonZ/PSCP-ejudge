"""Distribute"""
def main():
    money = 2
    son = 1
    max_money = (money-son)//7
    print(max_money)
    if son*8 < money:
        print(-1)
    elif money-max_money*8 <= 4:
        print(min(max_money-1, 0))
main()