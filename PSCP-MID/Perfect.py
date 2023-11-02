"""Perfect"""
def main(num, total=0):
    """Perfect"""
    for i in range(6, num):
        num_list = []
        for j in range(1, int(i**0.5)+1):
            if i%j == 0:
                num_list.append(j)
                num_list.append(i//j)
        total += sum(num_list)-max(num_list) if sum(num_list)-max(num_list) == i else 0
    print(total)
main(int(input()))
