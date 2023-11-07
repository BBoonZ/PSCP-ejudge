"""MissingNumber"""
def main(val_n):
    """set"""
    my_set2 = []
    my_set = set(i for i in range(1, val_n+1))
    while True:
        my_set2.append(int(input()))
        if my_set2[-1] == 0:
            del my_set2[-1]
            my_set2 = set(my_set2)
            break
    print(*sorted(my_set.difference(my_set2)), sep='\n')
main(int(input()))
