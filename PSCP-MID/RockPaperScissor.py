"""RockPaperScissor"""
def main():
    """เรื่องราวแห่งความรัก ครั้งหนึ่ง ที่เปื้อนด้วยรอยยิ้มและมีน้ำตาให้กับมัน """
    text = input()
    ppa = False
    ppb = False
    point_a = 0
    point_b = 0
    for i in range(len(text)):
        if not i%2:
            player_a = text[i]
            ppa = True
        else:
            player_b = text[i]
            ppb = True
        if ppa and ppb:
            ppa = False
            ppb = False
            if player_a == player_b:
                continue
            elif player_a == 'S':
                if player_b == 'P':
                    point_a += 1
                    continue
                point_b += 1
            elif player_a == 'R':
                if player_b == 'S':
                    point_a += 1
                    continue
                point_b += 1
            elif player_a == 'P':
                if player_b == 'R':
                    point_a += 1
                    continue
                point_b += 1
    compare(point_a, point_b)

def compare(point_a, point_b):
    """หากเปรียบดั่งดวงดาว คงสวยงาม ประดับประดาด้วยเรื่องราวที่คิดถึง"""
    if point_a > point_b:
        print("A win %d-%d"% (point_a, point_b))
    elif point_a < point_b:
        print("B win %d-%d"% (point_b, point_a))
    else:
        print("DRAW", point_a)
main()
