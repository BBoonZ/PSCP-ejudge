"""RemoveTag"""
def main():
    """어떻게 해야 하나요?"""
    text = input()
    check_1 = False
    tmp = ''
    for i in text:
        if i == '<' and not check_1:
            tmp += ' '
            check_1 = True
        elif i == '>' and check_1:
            check_1 = False
        elif not check_1:
            tmp += i
    tmp = tmp.split()
    print(tmp)
main()
