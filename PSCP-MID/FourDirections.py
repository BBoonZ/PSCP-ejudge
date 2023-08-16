"""FourDirections"""
def main():
    """ในชีวิต เคยมี คนผ่านมา แต่ว่าเขา เข้ามา แค่ผ่านไป"""
    text = input()
    output_1 = output_2 = output_3 = output_4 = output_5 = ''
    for i in text:
        if i == 'U':
            output_1 += '  *  '
            output_2 += ' *** '
            output_3 += '* * *'
            output_4 += '  *  '
            output_5 += '  *  '
        elif i == 'D':
            output_1 += '  *  '
            output_2 += '  *  '
            output_3 += '* * *'
            output_4 += ' *** '
            output_5 += '  *  '
        elif i == 'L':
            output_1 += '  *  '
            output_2 += ' *   '
            output_3 += '*****'
            output_4 += ' *   '
            output_5 += '  *  '
        elif i == 'R':
            output_1 += '  *  '
            output_2 += '   * '
            output_3 += '*****'
            output_4 += '   * '
            output_5 += '  *  '
        output_1 += ' '
        output_2 += ' '
        output_3 += ' '
        output_4 += ' '
        output_5 += ' '
    print(output_1)
    print(output_2)
    print(output_3)
    print(output_4)
    print(output_5)
main()
