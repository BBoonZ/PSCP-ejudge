"""ValidVar"""
def main():
    """Nissin"""
    rob = int(input())
    output = ''
    check = ['if', 'else', 'elif', 'while', 'for', 'True', 'False', 'continue',\
         'break', 'return', 'is', 'in', 'and', 'or', 'from', 'as', 'pass', 'not', 'def', 'None']
    for _ in range(rob):
        put = 'Valid\n'
        test = input()
        if test in check:
            put = 'Invalid\n'
        if test.isspace() or test[0].isnumeric():
            put = 'Invalid\n'
        for j in test:
            if not j.isalnum() and j != '_':
                put = 'Invalid\n'
                break
        output += put
    print(output)
main()
