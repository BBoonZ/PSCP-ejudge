"""Parity"""
def main():
    """a"""
    string = input()
    text = input()
    count = 0
    for i in string:
        if i == '1':
            count += 1
    if text == 'Even':
        if count%2 == 0:
            string += '0'
        else:
            string += '1'
    else:
        if count%2 == 0:
            string += '1'
        else:
            string += '0'
    print(string)
main()
