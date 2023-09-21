"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def main():
    """ห้ะ"""
    text = input().split()
    output = []
    for i in text:
        txt = ''
        if len(i) > 2:
            for j in i:
                if j.isalpha():
                    txt += j
            if len(txt) >= 2:
                output.append(txt)
    output.sort(key=ascii)
    if output != []:
        for i in output:
            print(i)
    else:
        print('Nope')
main()
