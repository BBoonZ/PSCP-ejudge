"""Cat Parade"""
def main():
    """หมา แมวไรไม่รู็"""
    cat_list = []
    check = []
    while True:
        cat = input()
        if cat == 'END':
            break
        if cat == "IT'S A DOG":
            cat_list.remove(cat_list[-1])
            continue
        if ',' in cat:
            cat = cat.split(',')
            for i in cat:
                cat_list.append(i.lstrip())
            continue
        cat_list.append(cat)

    cat_list2 = cat_list.copy()
    cat_list2.sort()
    for i in cat_list2:
        if i in check:
            continue
        if i not in check:
            check.append(i)
        for j in range(len(cat_list)):
            if i == cat_list[j]:
                print(i, j+1, cat_list2.count(i))
                break
main()
