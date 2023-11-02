"""[Recommended] Coke V2"""
import math

def coke(aaa, bbb, ccc, ddd):
    """coke"""
    total = 0
    if bbb == 0 and ddd != 0:
        total += aaa*ddd
    elif bbb != 0 and ccc != 0 and ddd != 0:
        if ddd%bbb != 0:
            total += ((aaa*(ddd-(ddd//bbb)))+(ccc*(ddd//bbb)))
        elif ddd%bbb == 0:
            total += ((aaa*(ddd-((ddd//bbb)-1)))+(ccc*((ddd//bbb)-1)))
    elif bbb != 0 and ccc == 0 and ddd != 0:
        if ddd%bbb == 0:
            total += ((aaa*(ddd-((ddd//bbb)-1)))+(ccc*((ddd//bbb)-1)))
        elif ddd%bbb != 0:
            total += ((aaa*(ddd-((ddd//bbb))))+(ccc*((ddd//bbb))))
    elif ddd == 0:
        total = 0
    return total

def main(price, far, pro_price, val):
    """i like coke"""
    for i in range(0, 100):
        val = i
        if far == 0:
            return print(val*price)
        price_1 = (val-math.ceil((val-far)/far))*price
        price_2 = math.ceil((val-far)/far)*pro_price
        
        if price_1+price_2 != coke(price, far, pro_price, val):
            print(i)
main(10, 3, 7, 0)


