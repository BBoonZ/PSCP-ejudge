"""Discount"""
def main():
    """เธอก็เหมือนหน้าหนังสือที่เราชอบเปิดไป #คำคมfifa"""
    for ren in range(1, 1000):
        book = []
        books = []
        for i in range(ren):
            val = 10
            book.append(int(val))
            book = sorted(book)
        #print(sum(book[len(book)//5:]) if len(book) != 5 else sum(book))
        boss = (sum(book[len(book)//5:]) if len(book) != 5 else sum(book))

        for i in range(ren):
            each = 10
            if each == 'ENTER':
                break
            books.append(int(each))
        if len(books) <= 5:
            karn = (sum(books))
        elif len(books) in range(6, 20):
            karn = (sum(sorted(books)[len(books)//5:]) if len(books) not in range(15, 20) else\
            sum(sorted(books)[2:]))
        else:
            karn = (sum(sorted(books)[len(books)//5:]))
        
        if boss != karn:
            print(ren, boss, karn)
main()
