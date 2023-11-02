"""GCD_v2"""
def main(num_1, num_2):
    """GCD"""
    num_1, num_2 = min(num_1, num_2), max(num_1, num_2)
    if num_1 == 0:
        return print(num_2)
    while True:
        num_1, num_2 = num_2%num_1, num_1
        if num_1 == 0:
            break
    print(num_2)
main(int(input()), int(input()))
