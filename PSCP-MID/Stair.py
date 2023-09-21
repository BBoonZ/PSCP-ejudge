"""Stair"""
def main():
    """maiyakmainya"""
    max_foot = int(input())
    kan = int(input())
    kung = 1
    nub = 0
    output = 0
    check = True
    for _ in range(kan):
        num = int(input())
        nub += num
        if num > max_foot:
            check = False
        if nub == max_foot:
            output += 1
            kung = 0
            nub = 0
            continue
        elif nub > max_foot:
            output += 1
            kung = 1
            nub = num
            continue
    if kung == 1 or nub != 0:
        output += 1
    if check:
        print(output)
    else:
        print("NO")
main()
