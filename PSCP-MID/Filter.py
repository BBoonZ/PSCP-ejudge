"""Filter"""
import json
def main():
    """Hold"""
    txt = json.loads(input())
    fite = float(input())
    nope = True
    txt = dict(sorted(txt.items(), key=lambda x: x))
    for i, j in txt.items():
        if float(j) >= fite:
            print("%s\t%.2f" %(i, j))
            nope = False
    if nope:
        print('Nope')
main()
