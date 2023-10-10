"""BookWorm"""
def main():
    """มันใช่ปะวะ"""
    rob = int(input())
    output = ''
    for _ in range(rob):
        time = int(input())
        book = []
        count = total = 0
        for j in range(int(input())):
            book.append(int(input()))
        book.sort()

        for j in book:
            total += j
            if total <= time:
                count += 1
        output += str(count) + '\n'
    print(output)
main()
