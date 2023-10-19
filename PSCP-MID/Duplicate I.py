"""Duplicate I"""
def main(num_m, num_n, set_a=''):
    """wawaaw"""
    for i in sorted(set(int(input()) for _ in range(num_m))\
    .intersection(set(int(input()) for _ in range(num_n))), reverse=True):
        set_a += str(i) + '\n'
    print(set_a if set_a != '' else 'Nope')
main(int(input()), int(input()))
