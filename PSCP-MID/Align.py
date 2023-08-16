"""Align"""
def main():
    """ทุกๆที ที่ฉันพยายามมองหน้าเธอ แต่สุดท้ายมันก็เบลอ กลายเป็นเขา"""
    size = int(input())
    tid = input()
    text = input()
    if tid == 'left':
        print(text + ' '*(size-len(text)))
    elif tid == 'center':
        print(' '*int(((size-len(text))/2+0.5)) + text + ' '*int(((size-len(text))/2)))
    elif tid == 'right':
        print(' '*(size-len(text)) + text)
main()