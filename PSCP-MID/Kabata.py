"""Kabata"""
def main():
    """bakkakataabaaa"""
    rob = int(input())
    output = ''
    for _ in range(rob):
        txt = input()
        txt = txt.replace('baka', 'z')
        txt = txt.replace('bakka', '')
        txt = txt.replace('ka', '')
        txt = txt.replace('ba', '')
        txt = txt.replace('ta', '')
        if not txt:
            output += 'yes\n'
        else:
            output += 'no\n'
    print(output)
main()
