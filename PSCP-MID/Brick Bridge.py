"""Brick Bridge"""
def main():
    """อิฐพร้อมก่อสุดหล่อพร้อมยัง"""
    brick_a = int(input())
    brick_b = int(input())
    goal = int(input())
    nub = 0
    if brick_b*5 > goal:
        nub = 5*int(goal/5)
    elif brick_b*5 <= goal:
        nub = brick_b*5
    if goal-nub <= brick_a:
        print(brick_a-((nub+brick_a)-goal))
    else:
        print(-1)
main()