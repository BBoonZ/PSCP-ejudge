"""ValidVar"""
def main():
    rob = int(input())
    output = ''
    check = ['if', 'else', 'elif', 'while', 'for', 'True', 'False', 'continue', 'break', 'return', 'is', 'in', 'and', 'or', 'from', 'as', 'pass', 'not', 'def', 'None']
    for i in range(rob):
        test = input()
        if test in check:
            output += 'Invalid\n'
            continue
        if test.isspace():
            print("w")
    print(output)
main()
