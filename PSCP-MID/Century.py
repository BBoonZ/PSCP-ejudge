"""Century"""
def main():
    """ปล่อยให้เวลาเป็นเรื่องของอนาคต"""
    nub = int(input())
    output = ''
    for _ in range(nub):
        pee = input()
        if pee[:4] == 'B.E.':
            _ad = (int(pee[5:])-543+99)//100
            if _ad <= 0:
                output += 'ERROR' + '\n'
                continue
            output += str(_ad) + '\n'
        else:
            _be = (int(pee[5:])+99)//100
            if _be <= 0:
                output += 'ERROR' + '\n'
                continue
            output += str(_be) + '\n'
    print(output)
main()
