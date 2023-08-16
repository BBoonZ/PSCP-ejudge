"""Stepper II"""
def main():
    """ค่อยๆเดินอย่าทำห้าว ระวังได้กินข้าวโรงบาล"""
    nub = int(input())
    nub2 = int(input())
    if nub < nub2:
        for i in range(nub, nub2+1):
            print(i)
    else:
        for i in range(nub, nub2-1, -1):
            print(i)
main()