"""Roman"""
def main(roman, total=0, last=0):
    """XX XX"""
    r_dict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    for i in reversed(roman):
        if r_dict.get(i) < last:
            total -= r_dict.get(i)
        else:
            total += r_dict.get(i)
        last = r_dict.get(i)
    print(total)
main(input())
