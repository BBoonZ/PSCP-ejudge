"""Classify"""
def main():
    """ยากน้าาา"""
    dic_id = {}
    check = ''
    while True:
        val = input()
        if val == 'END':
            break
        if val[:4] in dic_id:
            dic_id[val[:4]] += 1
        else:
            dic_id[val[:4]] = 1
    _id = sorted(dic_id.items(), key=lambda x: x[:4])
 
    for i in _id:
        if check != i[0][:2]:
            check = i[0][:2]
            print(i[0][:2], int(i[0][2:5]), i[1])
        elif check == i[0][:2]:
            print('--', int(i[0][2:5]), i[1])
main()
