"""[Recommended] Dart"""
def main(num):
    """Darttong Dartjai"""
    points_list = [input().split() for _ in range(num)]
    total_point = 0
    for i in points_list:
        point = (int(i[0])**2 + int(i[1])**2)**0.5
        if point <= 2:
            total_point += 5
        elif point <= 4:
            total_point += 4
        elif point <= 6:
            total_point += 3
        elif point <= 8:
            total_point += 2
        elif point <= 10:
            total_point += 1
    print(total_point)
main(int(input()))
