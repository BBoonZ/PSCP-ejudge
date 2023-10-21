"""Socks"""
def main():
    """sock so s?!k?"""
    txt = input()
    total = 0
    t_dict = {}
    out_list = []
    for i in txt:
        t_dict[i] = t_dict.get(i, 0) + 1
    t_dict_sort = sorted(t_dict.items(), key=lambda x: x[0])
    for i, j in t_dict_sort:
        out_list += (i*2 for _ in range(j//2))
        total += j//2
    if out_list != []:
        print(*out_list)
    else:
        print('None')
    print(total)
main()
