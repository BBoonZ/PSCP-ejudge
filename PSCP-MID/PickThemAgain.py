"""pickagain"""
def main():
    """pick"""
    check = 0
    mylist = input().split()
    for i in range(len(mylist) - 1, -1, -1):
        if int(mylist[i]) % 3 == 0 or int(mylist[i]) % 5 == 0:
            print(mylist[i])
            check = 1
    if check == 0:
        print('Nope')
main()
