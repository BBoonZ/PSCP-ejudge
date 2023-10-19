"""Easy Histogram"""
def main():
    """ไม่น้อยลงเลย"""
    txt = input()
    dic = {}
    for i in txt:
        if i.isalpha():
            dic[i] = dic.get(i, 0) + 1
    dic_sort = sorted(dic.keys(), key=lambda x: (x.lower(), x.isupper()))
    for i in dic_sort:
        print(i, '=', dic.get(i))
main()
