"""Shorten"""
def main():
    """เพื่อนกูคิดได้ไง"""
    check1 = check2 = False
    output = first_num = num_c = ''
    while True:
        num = int(input())
        if num == -1:
            output += str(first_num)
            if check2:
                output += '-' + str(num_c)
            break
        if not check1:
            first_num = num
            check1 = True
        elif num-num_c == 1:
            check2 = True
        else:
            output += str(first_num)
            if check2:
                output += '-' + str(num_c)
            output += ', '
            check2 = False
            first_num = num
        num_c = num
    print(output)
main()
