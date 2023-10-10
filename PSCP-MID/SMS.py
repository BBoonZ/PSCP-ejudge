"""SMS"""
def main():
    """กดๆๆๆๆๆตู๊ดๆๆๆๆๆ"""
    txt = int(input())
    output = []
    for _ in range(txt):
        num = int(input())
        time = int(input())
        if num == 1:
            for _ in range(time):
                if output != []:
                    del output[-1]
            continue
        output.append(check(num, time))
    if output == []:
        return print('null')
    print(*output, sep='')

def check(num, time):
    """check กดๆๆๆ"""
    num_2 = ['C', 'A', 'B', 'C']
    num_3 = ['F', 'D', 'E', 'F']
    num_4 = ['I', 'G', 'H', 'I']
    num_5 = ['L', 'J', 'K', 'L']
    num_6 = ['O', 'M', 'N', 'O']
    num_7 = ['S', 'P', 'Q', 'R', 'S']
    num_8 = ['V', 'T', 'U', 'V']
    num_9 = ['Z', 'W', 'X', 'Y', 'Z']
    if num == 2:
        val = num_2[time%3]
    elif num == 3:
        val = num_3[time%3]
    elif num == 4:
        val = num_4[time%3]
    elif num == 5:
        val = num_5[time%3]
    elif num == 6:
        val = num_6[time%3]
    elif num == 7:
        val = num_7[time%4]
    elif num == 8:
        val = num_8[time%3]
    elif num == 9:
        val = num_9[time%4]
    return val
main()
