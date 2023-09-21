"""Kaprekars"""
def main():
    """เราเจอกันในวันที่ตัวฉัน ยังไม่ค่อยเข้าใจว่าจริงๆแล้ว รักเป็นยังไง"""
    val = int(str(input()))
    i = 0
    while True:
        num_1, num_2, num_3, num_4 = mak(val)
        val_mak = int(num_1+num_2+num_3+num_4)
        val_noi = int(num_4+num_3+num_2+num_1)
        val = val_mak-val_noi
        i += 1
        if val_mak-val_noi == 6174:
            break
    print(i)

def mak(val):
    """s"""
    num_1 = val//1000%10
    num_2 = val//100%10
    num_3 = val//10%10
    num_4 = val%10
    if num_2 > num_1:
        num_1, num_2 = num_2, num_1
    if num_3 > num_2:
        num_2, num_3 = num_3, num_2
    if num_2 > num_1:
        num_1, num_2 = num_2, num_1
    if num_4 > num_3:
        num_3, num_4 = num_4, num_3
    if num_3 > num_2:
        num_2, num_3 = num_3, num_2
    if num_2 > num_1:
        num_1, num_2 = num_2, num_1
    return str(num_1), str(num_2), str(num_3), str(num_4)


main()
