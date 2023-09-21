"""Heron of Alexandria"""
def main():
    """AREA"""
    val_a = float(input())
    val_b = float(input())
    val_c = float(input())
    val_s = (val_a+val_b+val_c)/2
    result = (val_s*(val_s-val_a)*(val_s-val_b)*(val_s-val_c))**0.5
    print("%.3f"% result)
main()
