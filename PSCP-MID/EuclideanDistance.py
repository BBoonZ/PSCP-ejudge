"""EuclideanDistance"""
def main():
    """Calculate the Euclidean distance"""
    juut = int(input())
    total = 0
    x2_scale = 0
    y2_scale = 0

    for i in range(juut):
        scale = input()
        x1_scale, y1_scale = map(int, scale.split())

        if i != 0:
            total += ((x2_scale - x1_scale) ** 2 + (y2_scale - y1_scale) ** 2) ** 0.5

        x2_scale = x1_scale
        y2_scale = y1_scale

    print('%.2f' % total)

main()
