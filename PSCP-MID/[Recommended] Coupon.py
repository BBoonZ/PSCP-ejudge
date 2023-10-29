"""[Recommended] Coupon"""
def main():
    """The Final is great game bro"""
    val = float(input())
    total_1 = total_2 = 99999999
    check_1 = check_2 = True
    coupon_1 = input().split()
    coupon_2 = input().split()
    if float(coupon_1[1]) <= val:
        check_1 = False
        total_1 = float(val-float(coupon_1[0]))
        total_1 = max(0, total_1)
    if float(coupon_2[1]) <= val:
        check_2 = False
        total_2 = float(val-(val*float(coupon_2[0])/100))
        total_2 = max(0, total_2)

    if total_1 < total_2:
        print(1, '%.1f'%total_1)
    elif total_2 < total_1:
        print(2, '%.1f'%total_2)
    elif check_1 and check_2:
        print('Nope')
    elif total_1 == total_2:
        if float(coupon_1[1]) <= float(coupon_2[1]):
            print(1, '%.1f'%total_1)
        else:
            print(2, '%.1f'%total_2)
main()
