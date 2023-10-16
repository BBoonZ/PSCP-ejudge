"""MissingCard (No Set)"""
def main():
    """missing u"""
    all_card = ['AS', 'AH', 'AD', 'AC', 'KS', 'KH', 'KD', 'KC', 'QS', 'QH', 'QD', 'QC', \
    'JS', 'JH', 'JD', 'JC', '10S', '10H', '10D', '10C', '9S', '9H', '9D', '9C', '8S',\
     '8H', '8D', '8C', '7S', '7H', '7D', '7C', '6S', '6H', '6D', '6C', '5S', '5H', '5D',\
     '5C', '4S', '4H', '4D', '4C', '3S', '3H', '3D', '3C', '2S', '2H', '2D', '2C']
    card = [input() for _ in range(51)]
    check_card = [i for i in all_card if i not in card]
    print(*check_card)
main()
