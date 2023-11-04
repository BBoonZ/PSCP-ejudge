"""Compound Interest"""
def main(money, val_r, year):
    """i love money"""
    for _ in range(year):
        money += money*(val_r/100)
    print("%.2f" %money)
main(int(input()), float(input()), int(input()))
