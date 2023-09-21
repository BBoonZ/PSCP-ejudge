"""Restaurant"""
def main():
    """a"""
    val_a = float(input())
    val_b = float(input())
    val_c = float(input())
    val_d = float(input())
    dis = 0
    al_ = val_a+val_d
    if val_a == val_b:
        val_a = val_a*(1-(val_c*0.01))
    if al_ >= val_b:
        dis = al_*(1-(val_c*0.01))
    if val_a-dis > 0 and val_c != 100 and val_d != 0:
        print("Yes %.3f"% (abs(dis-val_a)))
    elif val_a-dis < 0:
        print("No %.3f"% (abs(dis-val_a)))
    else:
        print("Yes")
main()
