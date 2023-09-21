"""Longer"""
import math
def main():
    """Longer"""
    val_r = float(input())
    val_a = float(input())
    val_b = float(input())
    rec = 2*math.pi*val_r
    cir = (val_a+val_b)*2
    if rec > cir:
        print("Circle is longer")
        print("%.5f"% (rec-cir))
    elif rec < cir:
        print('Rectangle is longer')
        print("%.5f"% (cir-rec))
    else:
        print("Equal")
        print("%.5f"% 0)
main()
