"""[Recommended] Coke V2"""
import math
def main(price, far, pro_price, val):
    """i like coke"""
    if far == 0 or val == 0:
        return print(val*price)
    price_1 = (val-math.ceil((val-far)/far))*price
    price_2 = math.ceil((val-far)/far)*pro_price
    print(price_1+price_2)
main(int(input()), int(input()), int(input()), int(input()))
