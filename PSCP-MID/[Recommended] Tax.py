"""[Recommended] Tax"""
def main(age, cc_, total=0):
    """TAX"""
    age_dict = {5 : 0, 6 : 0.10, 7 : 0.20, 8 : 0.30, 9 : 0.40, 10 : .50}
    total += (cc_//600 >= 1)*600*0.5 + (cc_//600 < 1)*cc_*0.5
    total += max(((cc_-600)//1200 >= 1)*1200*1.50 + ((cc_-600)//1200 < 1)*(cc_-600)*1.50, 0)
    total += max((cc_-1800)*4, 0)
    for i, j in age_dict.items():
        if i >= age:
            total -= total*j
            break
        if age >= 10:
            total -= total*.5
            break
    print('%.2f' %total)
main(int(input()), int(input()))
