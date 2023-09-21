"""Stamps"""
import math
def main():
    """แถมเลยไอน้อง"""
    val_n = int(input())
    pmt = int(input())
    stm = int(input())
    stm_u = int(input())
    dis = int(input())
    stm_h = 0
    total = 0
    for _ in range(val_n):
        price = int(input())
        if stm_h >= stm_u:
            if (stm_h//stm_u)*dis >= price:
                stm_h -= math.ceil((price/dis))*stm_u
                price = 0
            else:
                price -= (stm_h//stm_u)*dis
                stm_h -= (stm_h//stm_u)*stm_u
        if price >= pmt:
            stm_h += stm*(price//pmt)
        total += price

    print(total, stm_h, sep='\n')
main()
