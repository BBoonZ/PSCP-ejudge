"""FOR!F-Ball"""
def main():
    """คิด(แต่ไม่)ถึง คิด คิด (แต่ไม่) ถึงเธอ คิด(แต่ไม่)ถึง คิด คิด (แต่ไม่) ถึงเธอ """
    text = input()
    ball_0 = 1
    ball_1 = 0
    ball_2 = 0
    for i in text:
        if i == 'A':
            ball_0, ball_1 = ball_1, ball_0
        elif i == 'B':
            ball_1, ball_2 = ball_2, ball_1
        else:
            ball_2, ball_0 = ball_0, ball_2
    if ball_0:
        print(1)
    elif ball_1:
        print(2)
    elif ball_2:
        print(3)
main()
