"""BreachTheDoor"""
def main():
    """ห้ะ"""
    text = input().split()
    output = []
    for i in text:
        txt = ''
        if len(i) > 6:
            for j in i:
                if j.isalpha():
                    txt += j
            if len(txt) > 6:
                output.append(txt)
    print(*output)
main()
