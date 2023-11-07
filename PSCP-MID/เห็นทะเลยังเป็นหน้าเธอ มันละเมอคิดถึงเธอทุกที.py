"""เห็นทะเลยังเป็นหน้าเธอ มันละเมอคิดถึงเธอทุกที"""
def main(shark):
    """under the sea"""
    my_sea = {
        ('BULL SHARK') : 'THE SHALLOW ZONE',
        ('CHAIN CATSHARK', 'GREAT WHITE SHARK', 'GUMMY SHARK', 'BLUE SHARK', \
        'MAKO SHARK') : 'THE TWILIGHT ZONE',
        ('FRILLED SHARK', 'GOBLIN SHARK', 'SIXGILL SHARK', 'GREENLAND SHARK', \
        'COOKIECUTTER SHARK') : 'THE MIDNIGHT ZONE',
        ('MEGAMOUTH SHARK') : 'THE ABYSSAL ZONE'
    }
    for i, j in my_sea.items():
        if i.count(shark):
            return print(j)
    print('ZONE JAI MA KLUNG RAK DUAY KAN MAI.')
main(input())
