"""Helloooo"""
def main():
    """ahlooo"""
    txt = input()
    output = ''
    for i in range(len(txt)-1, -1, -1):
        output += txt[i]
        if txt[i] in ['a', 'e' ,'i' ,'o', 'u']:
            output = output.replace(txt[i], txt[i]*4)[::-1]
            txt = txt[:i] + output
            break
    print(txt)
main()
