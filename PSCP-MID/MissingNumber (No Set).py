"""MissingNumber (No Set)"""
def main(val_n):
    """gim me set"""
    my_list = []
    while True:
        my_list.append(int(input()))
        if my_list[-1] == 0:
            del my_list[-1]
            break
    for i in range(1, val_n+1):
        if i not in my_list:
            print(i)
main(int(input()))
