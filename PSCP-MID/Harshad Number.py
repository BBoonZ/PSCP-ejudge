"""Harshad Number"""
def main():
    """ไอติมชาเขียวอร่อนจีงง"""
    output = ''
    for _ in range(10):
        num = str(abs(int(input())))
        check = 0
        for j in num:
            check += int(j)
        if check != 0 and int(num)%check == 0:
            output += 'Yes\n'
        else:
            output += 'No\n'
    print(output)
main()
