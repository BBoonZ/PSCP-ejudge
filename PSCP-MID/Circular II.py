"""LAB2"""
def main():
    """a"""
    pointx = float(input())
    pointy = float(input())
    ray = float(input())
    pointxn = float(input())
    pointyn = float(input())
    rayn = float(input())
    dis = ((pointxn-pointx)**2+(pointyn-pointy)**2)**0.5
    if dis >= ray+rayn:
        print("No")
    else:
        print("Yes")
main()