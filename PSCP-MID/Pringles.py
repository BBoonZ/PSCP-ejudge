"""Pringles"""
def main():
    """เมาส์อะไรไมรู้ของซีใช้ค่ตยาก"""
    text = input()
    mun = input()
    text = input()
    nil = int(input())
    output = ''
    count = 0
    for i in range(len(text)):
        if nil > i and mun[i] == ')':
            output += ' '
            count += 1
        elif nil > i:
            output += ' '
        else:
            output += mun[i]
    if ')' in output:
        print(count)
        print('There are still some left.')
        print(text)
        print(output+'|')
        print(text)
    else:
        print(count)
        print('None.')
        print(text)
        print(output+'|')
        print(text)
main()
