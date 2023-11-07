"""Pad Thai"""
def main():
    """i don't like Pad Thai ://////"""
    material = {
        'Pad Thai Sauce',
        'Tofu', 'Pickle Turnip',
        'Shrimp', 'Bean Sprouts',
        'Noodle', 'Chives', 'Lime',
        'Egg', 'Oil', 'Peanuts'
    }
    flavor = {'Sweet', 'Sour', 'Salty'}
    cook = set()
    flavor_2 = set()
    while True:
        val = input()
        if val == 'Cook':
            break
        cook.add(val)
    while True:
        val = input()
        if val == 'End':
            break
        flavor_2.add(val)

    if material.difference(cook) or cook.difference(material):
        for i in cook.difference(material):
            if i not in material:
                return print('This is not Pad Thai!!!')
        print('This is bad!')
    elif flavor_2.difference(flavor) or flavor.difference(flavor_2):
        print('Not Bad...')
    else:
        print('Delicious!')
main()
