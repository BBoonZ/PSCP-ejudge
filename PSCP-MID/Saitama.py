"""ฉันจะเป็น Saitama ให้ได้เลย"""
import math
def main():
    """Saitama"""
    n_wit = int(input())
    n_sit = int(input())
    n_luk = int(input())
    n_run = int(input())
    mpd_wit = n_wit/int(input())
    mpd_sit = n_sit/int(input())
    mpd_run = n_run/int(input())
    mpd_luk = n_luk/int(input())
    mn_day = find(mpd_wit, mpd_sit)
    mn_day = find(mn_day, mpd_luk)
    mn_day = find(mn_day, mpd_run)

    print(math.ceil(mn_day))


def find(val_1, val_2):
    """a"""
    if val_1 > val_2:
        return val_1
    return val_2
main()
