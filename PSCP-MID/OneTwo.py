"""OneTwo"""
def main(sn_):
    """FOUR!!"""
    if sn_ == 1:
        return '1'
    elif sn_ == 2:
        return '2'
    else:
        return str(main(sn_-1))+str(main(sn_-2))
print(main(int(input())))
