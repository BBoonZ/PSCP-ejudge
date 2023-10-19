"""Backward"""
def main():
    """main"""
    text = []
    while True:
        val = input()
        if val == 'NULL':
            break
        text.append(val)
    for i in range(len(text) - 1, -1, -1):
        print(text[i])
main()
