"""Lift"""
def main():
    """Lift ขึ้น Lift ลง"""
    kon = int(input())
    maz_weight = float(input())
    total = 0
    output = ''
    dek = False
    adult = False
    for _ in range(kon):
        age = int(input())
        weigth = float(input())
        if age < 12:
            dek = True
        else:
            adult = True
        total += weigth
    if dek and not adult:
        output += 'Not Safe'
    elif total > maz_weight:
        output += 'Not Safe'
    else:
        output += 'Safe'
    print(output)
main()
