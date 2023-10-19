"""ASc"""
def main():
    """ASC"""
    mylist = []
    for _ in range(5):
        mylist.append(int(input()))
    mylist.sort()
    for i in range(5):
        print(mylist[i])
main()
