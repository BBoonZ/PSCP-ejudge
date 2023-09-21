"""Milk"""
def main():
    """นมที่ดีคือ นมที่ดี Passed"""
    val_a = int(input())
    val_b = int(input())
    val_c = int(input())
    val_d = int(input())
    kod = val_d//val_a
    far = kod
    if val_b != 0:
        while True:
            if far < val_b:
                break
            else:
                kod += val_c
                far += val_c
                far -= val_b
    print(kod)
main()