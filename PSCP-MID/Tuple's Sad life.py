"""tf is Tuple"""
def main():
    """gongong"""
    tup = tuple(input().split())
    val = input()
    print(((str(tup.index(val)) +  ' ')*tup.count(val) + '\n')*tup.count(val))
main()
