"""Discount"""
def main():
    """เธอก็เหมือนหน้าหนังสือที่เราชอบเปิดไป #คำคมfifa"""
    book = []
    while True:
        val = input()
        if val == 'ENTER':
            break
        book.append(int(val))
    book = sorted(book)
    print(sum(book[len(book)//5:]) if len(book)%5 != 0 else sum(book[len(book)//5-1:]))
main()
