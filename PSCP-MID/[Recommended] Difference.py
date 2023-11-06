"""[Recommended] Difference"""
import json
def main(count=0):
    """MID DIFF"""
    list_a = json.loads(input())
    list_b = json.loads(input())
    dict_a, dict_b = {}, {}
    for i in list_a:
        dict_a[i] = dict_a.get(i, 0) + 1
    for i in list_b:
        dict_b[i] = dict_b.get(i, 0) + 1
    total_list = sorted(set(list_a).union(set(list_b)))
    for i in total_list:
        if abs(dict_a.get(i, 0)-dict_b.get(i, 0)) != 0:
            print(i, abs(dict_a.get(i, 0)-dict_b.get(i, 0)))
            count = 1
    if not count:
        print('ONAJI DAYO!')
main()
