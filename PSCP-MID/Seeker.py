"""Seeker"""
def main(txt, num=''):
    """find u aa"""
    num_list = []
    for i in txt:
        if i.isalpha():
            continue
        else:
            num += i
        if num != '':
            num_list.append(num)
            num = ''
    print(num_list)
main(input()+'a')
