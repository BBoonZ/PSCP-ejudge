"""LAB1"""
def main():
    """LAB"""
    val_a = float(input())
    val_b = float(input())
    val_c = float(input())
    val_d = float(input())
    print(fff(fff(val_a)))
    print(ggg(fff(val_a-val_b)))
    print(hhh(fff(val_a+val_b), fff(val_a+val_c), ggg(fff(val_d**2))))
    print(iii(hhh(fff(val_a+val_b), fff(val_a-val_c), ggg(fff(val_d**2))), \
    ggg(fff(val_a-val_b)), fff(fff(fff(fff(fff(val_c))))), val_d**8))
def fff(val_a):
    """f"""
    return 2*val_a
def ggg(val_a):
    """g"""
    return 3*val_a**4-val_a**3+2*val_a**2+10
def hhh(val_a, val_b, val_c):
    """hhh"""
    return ((val_c+val_a)**2)-val_a*val_b+val_b**2
def iii(val_a, val_b, val_c, val_d):
    """i"""
    return (val_a**2+val_b**2-val_c**2)/(val_d**2-2*val_a*val_d+2*val_a)
main()