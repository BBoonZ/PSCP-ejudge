"""PH"""
def main():
    """PH"""
    val = float(input())
    if 0 <= val < 7:
        print('acidic')
    elif val == 7:
        print('neutral')
    elif 7 < val <= 14:
        print('akaline')
    else:
        print('error')
main()
