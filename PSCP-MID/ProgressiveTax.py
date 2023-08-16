"""ProgressiveTax"""
def main():
    """บิ๊กป้อม บิ๊กป๊อก บิ๊กตู่"""
    my_money = int(input())
    pay = 0
    if my_money >= 4000000:
        pay += int((my_money-4000000)*0.35)
        my_money -= my_money-4000000
    if my_money >= 2000000:
        pay += int((my_money-2000000)*0.30)
        my_money -= my_money-2000000
    if my_money >= 1000000:
        pay += int((my_money-1000000)*0.25)
        my_money -= my_money-1000000
    if my_money >= 750000:
        pay += int((my_money-750000)*0.20)
        my_money -= my_money-750000
    if my_money >= 500000:
        pay += int((my_money-500000)*0.15)
        my_money -= my_money-500000
    if my_money >= 300000:
        pay += int((my_money-300000)*0.10)
        my_money -= my_money-300000
    if my_money >= 150000:
        pay += int((my_money-150000)*0.05)
        my_money -= my_money-150000
    print(int(pay))
main()
