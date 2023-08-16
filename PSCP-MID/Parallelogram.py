"""Parallelogram"""
def main():
    """ก่อนที่เธอจะลืมฉันไป"""
    text = input()
    for i in range(1, len(text)+1):
        print(" "*(len(text)-i), end='')
        print(text[:i])
    for i in range(1, len(text)+1):
        print(text[i:])
main()
