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
    if len(book)//5 == 3:
        return print(sum(book[len(book)//5-1:]))
    print(sum(book[len(book)//5:]) if len(book) != 5 else sum(book))
main()
