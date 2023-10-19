"""HorizontalHistogram"""
def main():
    """Flower and Wine"""
    txt = input()
    dic_txt = {}
    for i in txt:
        dic_txt[i] = dic_txt.get(i, 0) + 1
    dic_txt = dict(sorted(dic_txt.items(), key=lambda x: (not x[0].islower(), x)))
    for i in dic_txt:
        tran = ''
        for j in range(dic_txt.get(i)):
            if j%5 == 0 and j != dic_txt.get(i) and j != 0:
                tran += '|'
            tran += '-'
        print(i, ':', tran)
main()
