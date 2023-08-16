"""Run Length Encoding"""
def main():
    """อย่ามาเล่นตลก กับความรู้สึกคน เพราะแม่งไม่ตลก"""
    text = input()
    output = ''
    count = 1
    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            output += str(count) + text[i-1]
            count = 1
    i = len(text)
    output += str(count) + text[i-1]
    print(output)
main()
