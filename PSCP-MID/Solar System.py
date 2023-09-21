"""Solar System"""
def main():
    """ttor"""
    text = input()
    _al = text.count(' ')+1
    f_sun = 0
    for i in range(len(text)):
        if text[i].isspace():
            f_sun += 1
        if text[i:i+5] == ' Sun ':
            break
        if text[i:i+4] == 'Sun ' and i == 0:
            break

    cool_1, cool_2 = find_c(text, _al)
    hot_1, hot_2 = find_h(text, f_sun)
    if f_sun > _al-f_sun-1:
        if hot_1 == '':
            print('Hot:%s %s'% (hot_1, hot_2))
        else:
            print('Hot: %s %s'% (hot_1, hot_2))
        print('Cool: %s'% cool_1)
    elif f_sun < _al-f_sun-1:
        if hot_1 == '':
            print('Hot:%s %s'% (hot_1, hot_2))
        else:
            print('Hot: %s %s'% (hot_1, hot_2))
        print('Cool: %s'% cool_2)
    else:
        print('Hot: %s %s'% (hot_1, hot_2))
        print('Cool: %s %s'% (cool_1, cool_2))


def find_c(text, al_):
    """cool cool"""
    cool_1 = cool_2 = ''
    count = 0
    for i in range(len(text)):
        if text[i].isspace():
            count += 1
        elif count == 0:
            cool_1 += text[i]
        elif count == al_-1:
            cool_2 += text[i]
    return cool_1, cool_2

def find_h(text, f_sun):
    """hot hot"""
    hot_1 = hot_2 = ''
    count = 0
    for i in range(len(text)):
        if text[i].isspace():
            count += 1
        elif count == f_sun-1:
            hot_1 += text[i]
        elif count == f_sun+1:
            hot_2 += text[i]
    return hot_1, hot_2
main()
