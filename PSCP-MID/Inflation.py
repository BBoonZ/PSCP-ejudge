"""Inflation"""
def main():
    """ummy Yummy Yummy Yummy Yummy Yummy"""
    val_n = float(input())
    val_k = int(input())
    money = val_n
    for _ in range(val_k):
        money = round(money*(1+0.0381)-0.005, 2)
    print('%.02f'% (money-0.005))
main()
