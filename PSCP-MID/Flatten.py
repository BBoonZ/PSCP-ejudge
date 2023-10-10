"""Flatten"""
import json
def main():
    """แบนเรียบเลยยไอน้อง"""
    txt = json.loads(input())
    decode2 = txt.copy()
    decode = []
    while True:
        txt = decode2.copy()
        decode2 = []
        count = 1
        for i in txt:
            if isinstance(i, (float, int)):
                decode.append(i)
            else:
                decode2.extend(i)
                count = 0
        if count:
            break
    print(sorted(decode, reverse=True))
main()
