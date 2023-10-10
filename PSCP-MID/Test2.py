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
    print(new)
main()
