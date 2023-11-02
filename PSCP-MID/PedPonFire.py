"""PedPonFire"""
def main(val, count=0):
    """ห"""
    ped_list = [int(input()) for _ in range(val)]
    val_k = int(input())
    for i in ped_list:
        ped = ped_list[ped_list.index(abs(i-val_k))] if abs(i-val_k) in ped_list else 99999
        if i + ped == val_k:
            ped_list.remove(i)
            ped_list.remove(ped)
            count += 2
    print(count)
main(int(input()))
