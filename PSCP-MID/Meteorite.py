"""Meteorite"""
def main():
    """yakmak"""
    weight = float(input())
    gajry = int(input())
    weight2 = float(input())
    count = 0
    i = 0
    while True:
        if weight < weight2:
            break
        weight /= gajry
        count += gajry**i
        i += 1
    print(count)
main()
