"""Bad Keyboard"""
def main():
    """www awd Bad Keyboard"""
    text = input()
    output = ''
    for i in text:
        if i == 'o':
            output += 'i'
        elif i == 'i':
            output += 'o'
        elif i == 'O':
            output += 'I'
        elif i == 'I':
            output += 'O'
        else:
            output += i
    print(output)
main()
