"""[Recommended] Pro"""
def main():
    """pudding in hotpot is so sweettt"""
    val_x = int(input())
    val_y = int(input())
    price = int(input())
    people = int(input())

    print((people//val_x*val_y*price)+(people-people//val_x*val_x)*price)
main()
