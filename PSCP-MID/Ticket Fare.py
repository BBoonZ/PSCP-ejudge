"""Ticket Fare"""
def main():
    """ลงอโศก ต่อ mrt ไปบางหว้า กับ ลงหัวลำโพง ต่อ mrt ไปบางหว้า อะไรเร็วกว่ากัน???"""
    val_n, val_a, val_b, val_c, val_d, val_e, val_f, val_g = \
    int(input()), int(input()), int(input()), int(input()), \
    int(input()), int(input()), int(input()), int(input())

    if (val_g > val_n or val_g < 1) or (val_f > val_n or val_f < 1):
        print('Error')
    else:
        if abs(val_f-val_g) <= val_a:
            print(val_b)
        elif abs(val_f-val_g) <= val_a+val_c:
            print(val_b+val_d*abs(val_a-abs(val_f-val_g)))
        elif abs(val_f-val_g) > val_a+val_c:
            print((val_b+val_d*abs(val_c))+(val_e*abs(val_a+val_c-abs(val_f-val_g))))
main()
