"""Niwarn World"""
import math
def main():
    """midterm"""
    val_n = float(input())
    val_s = float(input())
    val_k = float(input())
    print("X: %.1f, Y: %.1f, Z: %.1f" \
    %(fun_x(val_n), fun_y(val_n, val_s), fun_z(val_k)))

def fun_x(val_n):
    """fun_x"""
    total = (math.log2(val_n**2)/\
    (2*val_n*math.log2(val_n)))+2
    return total

def fun_y(val_n, val_s):
    """fun_y"""
    total = (math.sin(math.radians(30))+\
    ((val_s*2)**0.5))/(fun_x(val_n)+3)
    return total

def fun_z(val_k):
    """fun_z"""
    total = ((8456*(fun_x(val_k)**4))/\
    (val_k*24))+fun_y(val_k, val_k)**2
    return total
main()
