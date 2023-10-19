"""LetterFrequency"""
def main(txt):
    """1 2 3 4 5"""
    dic_txt = {}
    for i in txt:
        if i.isalpha():
            dic_txt[i] = dic_txt.get(i, 0) + 1
    print(sorted(dic_txt.items(), key=lambda x: x[1], reverse=True)[0][0])
main(input().lower())
