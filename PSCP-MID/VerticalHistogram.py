"""VerticalHistogram"""
def main(txt):
    """ปวดคอจังวะ"""
    t_dict = {}
    for i in txt:
        t_dict[i] = t_dict.get(i, 0) + 1
    t_dict = dict(sorted(t_dict.items(), key=lambda x: (not x[0].islower(), x)))
    for i in range(max(t_dict.values()), 0, -1):
        print('%03d' %i, end=' ')
        for j in t_dict.values():
            if j < i:
                print(' ', end=' ')
            else:
                print('*', end=' ')
        print()
    print('   ', *t_dict.keys())
main(input())
