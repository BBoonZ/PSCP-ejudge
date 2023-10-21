"""Water"""
def main():
    """ลิ้นจี่เปรี้ยวจัด"""
    month = int(input())
    val_a = float(input())
    val_b = float(input())
    val_c = float(input())
    val_d = float(input())
    water_list = [float(input()) for _ in range(month)]
    out_list = []
    for i in water_list:
        total = 0
        total += min(i, val_b)*val_a
        if i > val_b:
            total += (i-val_b)*val_c
        total = (total > val_d)*total
        out_list.append(total)
    print('%.2f' %sum(out_list))
main()
