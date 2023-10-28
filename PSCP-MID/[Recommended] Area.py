"""[Recommended] Area"""
def main(val):
    """Area"""
    txt = [input() for _ in range(val)]
    count = 0
    for i in txt:
        for j in i:
            if j == ' ':
                continue
            count += 1
    print(count)
main(int(input()))
