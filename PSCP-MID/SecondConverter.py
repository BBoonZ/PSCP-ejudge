"""SecondConverter"""
def main():
    """SecondConverter"""
    val_k = int(input())
    val_s = int(input())
    val_m = int(input())
    val_h = int(input())

    new_s = val_k%val_s
    new_m = (val_k//val_s)%val_m
    new_h = ((val_k//val_s)//val_m)%val_h
    print("%d:%d:%d"% (new_h, new_m, new_s))
main()
