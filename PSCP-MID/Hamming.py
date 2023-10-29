"""Hamming"""
def main(txt_1, txt_2, count=0):
    """Hamming"""
    for i in range(len(txt_1)):
        if txt_1[i] != txt_2[i]:
            count += 1
    print(count)
main(input(), input())
