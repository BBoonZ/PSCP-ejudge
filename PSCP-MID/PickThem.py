"""pick"""
def main():
    """pick"""
    import json
    check = 0
    mylist = json.loads(input())
    for i in mylist:
        if i % 2 == 0:
            print(i)
            check = 1
    if check == 0:
        print('Nope')
main()
