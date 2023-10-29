"""[Recommended] Coupon"""
def main():
    """The Final is great game bro"""
    val = int(input())
    total_1 = total_2 = 0
    coupon_1 = input().split()
    coupon_2 = input().split()
    if int(coupon_1[1]) <= val:
        total_1 = float(val-int(coupon_1[0]))
    if int(coupon_2[1]) <= val:
        total_2 = float(val-(val*int(coupon_2[0])/100))

    if total_1 < total_2:
        print(1, total_1)
    elif total_2 < total_1:
        print(2, total_2)
    elif total_1 == 0 and total_2 == 0:
        print('Nope')
    elif total_1 == total_2:
        if coupon_1[1] < coupon_2[1]:
            return print(1, total_1)
        print(2, total_2)
main()
