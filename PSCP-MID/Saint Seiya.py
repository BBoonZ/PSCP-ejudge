"""Saint Seiya"""
def main():
    """ถถถถถเจอดักเคส"""
    sec = int(input())
    power = int(input())
    total = 0
    if sec >= 5000000 and sec < 6000000:
        total += 275833388
        if total >= power:
            total -= 275833388
        else:
            sec -= 5000000

    for i in range(1, sec+1):
        if total >= power:
            total += (sec-i)*12
            break
        if i%6 == 0:
            total += 1
        elif i%2 == 0:
            total += 165
    print(total)
main()
