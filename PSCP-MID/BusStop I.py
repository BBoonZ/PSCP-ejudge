"""BusStop I"""
def main():
    """yark na"""
    ppl = int(input())
    sign = int(input())
    count = 0
    car = []
    check_s = []
    new = []
    for i in range(sign):
        new.append(input().split())
    new.sort(key=lambda x: int(x[0]))

    for i in range(len(new)):
        txt = new[i]
        check_s.append(txt[0])
        del txt[0]
        for j in txt:
            if j not in check_s:
                car.append(j)
        del car[ppl+car.count(check_s[i]):]
        count += car.count(check_s[i])
        while check_s[i] in car:
            car.remove(check_s[i])
    print(count)
main()
