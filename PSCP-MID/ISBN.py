"""ISBN"""
def main(val):
    """ISBN"""
    total = -(10*int(val[0])+9*int(val[1])+8*int(val[2])\
    +7*int(val[4])+6*int(val[5])+5*int(val[6])\
    +4*int(val[8])+3*int(val[9])+2*int(val[10]))%11
    if total == 10:
        total = 'X'
    if str(total) == val[-1]:
        print('Yes')
    else:
        print('No', total)
main(input())
