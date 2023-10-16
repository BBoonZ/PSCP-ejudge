"""Seeker"""
def main(txt):
    """find u aa"""
    for i in txt:
        if not i.isnumeric():
            txt = txt.replace(i, ' ')
    txt = txt.split()
    print(sum(int(i) for i in txt))
main(input()+'a')
