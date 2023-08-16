"""GraderMachine"""
def main():
    """ไม่ชอบอ้อนเท่าไหร่ ชอบโอนมากกว่า"""
    nub = int(input())
    nub2 = int(input())
    val_sum = 0
    print("pass : ", end='')
    if nub > nub2:
        for i in range(nub, nub2-1, -1):
            if i%2 == 0:
                print(i, end=' ')
                val_sum += i
        print("\nSum :", val_sum)
    else:
        for i in range(nub, nub2+1):
            if i%2 == 0:
                print(i, end=' ')
                val_sum += i
        print("\nSum :", val_sum)
main()