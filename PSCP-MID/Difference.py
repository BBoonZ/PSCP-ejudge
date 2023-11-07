"""Difference"""
def main():
    """set sett zed??"""
    val_n = int(input())
    val_m = int(input())
    set_a = set()
    set_b = set()
    for _ in range(val_n):
        set_a.add(int(input()))
    for _ in range(val_m):
        set_b.add(int(input()))
    print(*sorted(set_a.difference(set_b)))
main()
