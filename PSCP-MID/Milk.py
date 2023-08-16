"""Milk"""
def main():
    bath = int(input())
    far = int(input())
    free = int(input())
    money = int(input())
    free_m = 0
    if far == 0:
        pack_m = money//bath
    else:
        pack_m = money//bath
        free_m = pack_m//far*free
    print(int(pack_m+free_m))
main()
