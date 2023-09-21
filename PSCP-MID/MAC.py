"""MAC"""
def main():
    """count ง่ายกว่า"""
    mac = ' ' + input()
    case = '0123456789abcdefgABCDEFG'
    valid_1 = valid_2 = valid_3 = valid_e = False
    for i in range(1, len(mac)):
        if (i%3 == 0 and mac[i] in ['-']) or mac[i] in case and mac.count('-') == 5:
            valid_1 = True
        elif (i%3 == 0 and mac[i] in [':']) or mac[i] in case and mac.count(':') == 5:
            valid_2 = True
        elif (i%5 == 0 and mac[i] in ['.']) or mac[i] in case and mac.count('.') == 2:
            valid_3 = True
        else:
            valid_e = True

    if valid_e:
        print('ERROR')
    elif valid_1:
        print('VALID 1')
    elif valid_2:
        print('VALID 2')
    elif valid_3:
        print('VALID 3')

main()
