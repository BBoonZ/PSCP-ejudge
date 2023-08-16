"""Table I"""
def main():
    """a"""
    val = input()
    virus = 0
    for i in val:
        if i == 'o':
            virus += 1
    print(virus)
main()