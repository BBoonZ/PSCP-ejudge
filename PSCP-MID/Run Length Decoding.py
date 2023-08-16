"""Run Length Decoding"""
def main():
    """ลาเธอได้สักที ลาก่อนให้เธอโชคดี ฉันยังจำได้อยู่เลย ที่เคยผ่านมาด้วยกัน"""
    text = input()
    num = ''
    output = ''
    for i in range(0, len(text)):
        if text[i].isnumeric():
            num += str(text[i])
        else:
            output += text[i]*int(num)
            num = ''
    print(output)
main()
