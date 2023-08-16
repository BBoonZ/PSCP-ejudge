"""Sequence X"""
def main():
    """วันนี้มันโคตรจะเฉาเหลือเกิน ฉันโคตรจะเกลียดหน้าเขา \
        อยากเดินไปคุยกับเสา แล้วจินตนาการว่าเสาเป็นหน้าเขาสักที"""
    val = int(input())
    print(("%02d "% 1)*(val*2-1))
    for i in range(2, val*2):
        if i-1 <= val:
            #ครึ่งบน
            if i == 2:
                continue
            for j in range(1, i):
                #print ครึ่ง
                print("%02d"% j, end=' ')
                if j == i-1:
                    #*จำนวนหลัง 01 02 to 01 02 02
                    print(("%02d "% j)*(val-1-i+2), end='')
                    print(("%02d "% j)*(val-1-i+2), end='')
            for j in range(i-1, 1, -1):
                #ข้างหลัง
                print("%02d"% (j-1), end=' ')
            print()
        else:
            break
    for i in range(val, 2, -1):
        #ครึ่งล่าง
        for j in range(1, i):
            #print ครึ่ง
            print("%02d"% j, end=' ')
            if j == i-1:
                #*จำนวนหลัง 01 02 to 01 02 02
                print(("%02d "% j)*(val-1-i+2), end='')
                print(("%02d "% j)*(val-1-i+2), end='')
        for j in range(i-1, 1, -1):
            #ข้างหลัง
            print("%02d"% (j-1), end=' ')
        print()
    if val != 1:
        print(("%02d "% 1)*(val*2-1))
main()