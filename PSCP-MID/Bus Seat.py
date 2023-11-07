"""Bus Seat"""
def main(row, val, column):
    """bus poon boon booonnn"""
    bus = [[row*i for i in range(1, val+1)]]
    for i in range(row-1):
        bus.append([bus[i][j]-1 for j in range(val)])
    for i in range(len(bus)):
        if i%2 == 0 and i != 0:
            print()
        for j in bus[i]:
            if column == j:
                print('XX', end=' ')
            else:
                print('%02d' %j, end=' ')
        print()
main(int(input()), int(input()), int(input()))
