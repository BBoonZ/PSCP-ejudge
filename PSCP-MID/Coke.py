"""Coke"""
def main():
    """coca cola"""
    bath = int(input())
    far = int(input())
    newbath = int(input())
    need = int(input())
    price = 0
    for i in range(1, need+1):
        if far != 0 and i != need and i%far == 0:
            price += newbath
        else:
            price += bath
    print(price)
main()
