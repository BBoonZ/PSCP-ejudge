"""Calculator"""
def main():
    """len!!!"""
    num = int(input())
    count = 1
    if num != 1:
        count = 0
        for i in range(1, num+1):
            count += len(str(i))+1
    print(count)
main()
