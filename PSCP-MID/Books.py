"""Books"""
import math
def main():
    """นั่งคิดตึ้งนานเลยน้า"""
    book = int(input())
    bpp = int(input())
    val_x = int(input())
    val_y = int(input())
    day = 0
    for i in range(book):
        total = 0
        count = 0
        while True:
            if total >= bpp:
                break
            total += math.ceil((val_x+day)/(val_y+day)*bpp)
            day += 1
            count += 1
        if count == 1:
            day += book-i-1
            break
    print(day)
main()
