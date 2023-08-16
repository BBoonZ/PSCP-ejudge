"""Largest Number"""
def main():
    """ใจสั่นๆ นึกว่าเศร้า ที่ไหนได้หิวเหล้า"""
    val_1 = (input())
    val_2 = (input())
    val_3 = (input())
    my_list = []
    my_list.append(val_1+val_2+val_3)
    my_list.append(val_1+val_3+val_2)
    my_list.append(val_2+val_3+val_1)
    my_list.append(val_2+val_1+val_3)
    my_list.append(val_3+val_1+val_2)
    my_list.append(val_3+val_2+val_1)
    val = find(my_list[0], my_list[1])
    val = find(val, my_list[2])
    val = find(val, my_list[3])
    val = find(val, my_list[4])
    val = find(val, my_list[5])
    print(int(val))
 
def find(val1, val2):
    """min max"""
    if val1 > val2:
        return val1
    return val2
main()