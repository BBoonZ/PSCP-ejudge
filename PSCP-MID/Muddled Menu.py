"""Muddled Menu"""
def main():
    """หลอกเยอะจังน้าา"""
    menu = []
    while True:
        text = input()
        if text == 'DONE':
            break
        if text == 'CLOSED':
            menu = []
            break
        if 'Can\'t do:' in text:
            menu.remove(text[text.find(':')+2:])
            continue
        if 'SOMETHING\'S WRONG' in text:
            menu = []
            continue
        if text[text.find('#')+1:] != 'N':
            menu.insert(int(text[text.find('#')+1:])-1, text[:text.find('#')-1])
        else:
            menu.append(text[:text.find('#')-1])
    print('Full Course:', menu, end=' ')
    menu.reverse()
    print('Reversed:', menu)
main()
