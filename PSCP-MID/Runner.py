"""Runner"""
def main():
    """plssss"""
    meter = int(input())
    kon = int(input())
    runner_c = []
    out = False
    for i in range(kon):
        runner_c.append(input().split())
    while True:
        for i in range(kon):
            runner_c[i][0] = int(runner_c[i][0]) + int(runner_c[i][0])
        for i in range(len(runner_c)):
            if int(runner_c[i][0]) + int(runner_c[i][1]) >= meter:
                runner_c[i][0] = int(runner_c[i][0]) + int(runner_c[i][1])
                out = True
        if out:
            break
    print(runner_c.index(max(runner_c))+1)
main()
