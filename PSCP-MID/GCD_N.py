"""GCD_N"""
def find(num_1, num_2):
    """GCD"""
    num_1, num_2 = min(num_1, num_2), max(num_1, num_2)
    if num_1 == 0:
        return print(num_2)
    while True:
        num_1, num_2 = num_2%num_1, num_1
        if num_1 == 0:
            break
    return num_2

def main(num):
    """GCD"""
    val = [int(input()) for _ in range(num)]
    last_num = val[0]
    for i in val:
        last_num = find(i, last_num)
    print(last_num)
main(int(input()))
