"""LAB1"""
def main():
    """LAB"""
    val_x = float(input())
    sec = int(val_x%60)
    mins = int(val_x//60%60)
    hour = int(val_x//60/60%24)
    days = int(val_x//60//60//24)
    if days >= 10000:
        print("ERR_:__:__:__")
    else:
        print("%04d:%02d:%02d:%02d"% (days, hour, mins, sec))
main()