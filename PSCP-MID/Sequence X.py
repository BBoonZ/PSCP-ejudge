"""Sequence X"""
def main():
    """ที่เธอบอกคำนั้นที่เธออยากให้ฉันอยู่"""
    val = int(input())
    for i in range(1, val+1):
        for _ in range(val-i):
            print("  ", end=' ')
        for j in range(i):
            print("%02d"% (j+1), end=' ')
        for j in range(i-1, 0, -1):
            print("%02d"% j, end=' ')
        print()
 
    for i in range(1, val+1):
        for _ in range(i):
            print("  ", end=' ')
        for j in range(0, val-i):
            print("%02d"% (j+1), end=' ')
        for j in range(val-i-1, 0, -1):
            print("%02d"% j, end=' ')
        print()
main()