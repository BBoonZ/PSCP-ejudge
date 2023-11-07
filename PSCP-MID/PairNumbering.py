"""PairNumbering"""
import json
def main(list_a, list_b, val_p, total=0):
    """ตะเกียบยังมีคู่ ทำไมรองเท้ามี 2 ข้าง"""
    check_set = set([i for i in list_a if i <= val_p])
    for i in check_set:
        if val_p - i in list_b:
            total += list_a.count(i)*list_b.count(val_p-i)
    print(total)
main(json.loads(input()), json.loads(input()), int(input()))
