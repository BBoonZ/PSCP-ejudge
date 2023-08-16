"""DAY1"""
def main():
    """A"""
    num = int(input())
    print("%.2f" %(fff(ggg(num))))
    print("%.2f" %(ggg(fff(num))))
def fff(xxx):
    """w"""
    return 2*xxx
def ggg(xxx):
    """w"""
    return xxx/2+1
main()