"""GCD_v1"""
def main():
    """ิิิิ"""
    val = int(input())
    val2 = int(input())
    val, val2 = max(val, val2), min(val, val2)
    num = val
    for i in range(1, val2+1):
        if val%i == 0 and val2%i == 0:
            num = i
    if num == 1:
        print('YES\n1')
    else:
        print('NO')
        print(num)
main()
