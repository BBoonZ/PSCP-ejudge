"""Factors"""
def main():
    """fac"""
    val_list = [int(input()) for _ in range(int(input()))]
    out_list = []
    output = ''
    for i in val_list:
        check = i
        num_dict = {}
        while True:
            if check <= 1:
                break
            for j in range(2, i+1):
                if check%j == 0:
                    num_dict[j] = num_dict.get(j, 0) + 1
                    check //= j
                    break
        out_list.append(num_dict)
    for i in out_list:
        output = ''
        for j, k in i.items():
            if k != 1:
                output += ('%d**%d x ' %(j, k))
            else:
                output += ('%d x ' %(j))
        print(output[:-2])
main()
