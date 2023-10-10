"""AndAgainAndAgainAndAgainAndAgainAndAgainAndAgain"""
def main():
    """ห้ะ"""
    txt = input().split()
    ae_ = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    output = []
    for i in txt:
        check = ''
        count = 0
        for j in i:
            if j in ae_ and len(i) >= 2:
                count += 1
        for j in i:
            if count >= 2 and j != '.':
                check += j
        if check != '':
            output.append(check)
    if output == []:
        return print('Nope')
    output.sort()
    print(*output, sep='\n')
main()
