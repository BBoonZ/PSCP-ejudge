"""Repeater"""
def main():
    """ทักไปเป็นร้อย โทรไปก็ไม่รับ"""
    text = input()
    for _ in range(100):
        print(text)
main()