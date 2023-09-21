"""Runner"""
def best_v(val):
    """เรียงอัตราเร็ว"""
    return val[0]

def main():
    """วิ่งตอนนี้เรียก ออกกำลังกาย วิ่งตอนใกล้ตายเรียก กายภาพ"""
    vec = int(input())
    val_n = int(input())
    my_list = []
    for i in range(val_n):
        my_list.append(input())
    my_list2 = my_list.copy()
    my_list.sort(key=best_v, reverse=True)

    i = 1
    output = ''
    while True:
        for j in my_list:
            total = int(j[0])*i + int(j[-1])
            if total >= vec:
                output = j
                break
        if output != '':
            break
        i += 1
    print(my_list2.index(output)+1)
main()