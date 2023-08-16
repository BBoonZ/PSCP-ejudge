"""Donut"""
def main():
    """โดนัทยังมีรู เมื่อไหร่ยูจะมีใจ"""
    bath = int(input())
    piece = int(input())
    free = int(input())
    need = int(input())
    mix = int(need/(piece+free))
    if mix*(piece+free) == need:
        buy = mix*piece*bath
        mix = mix*(piece+free)
    elif mix*(piece+free)+piece >= need:
        buy = mix*piece*bath + ((need-(mix*(piece+free)))*bath)
        mix += need-mix
        if mix-(int(need/(piece+free))*(piece+free)) == piece:
            mix += free
    else:
        mix = mix*(piece+free)+piece+free
        buy = int((mix/(piece+free))*bath*piece)
    print(buy, mix)
main()


def donut(price, numget, numfree, numneed):
    box = numget + numfree
    price_per_box = price*numget
    numbox = numneed//box
    remain = numneed - (numbox*box)
    if remain >= numget:
        numbox = numbox + 1
        remain = 0
    total_price = numbox*price_per_box + remain*price
    total_piece = numbox*box + remain
    return total_price, total_piece
 
