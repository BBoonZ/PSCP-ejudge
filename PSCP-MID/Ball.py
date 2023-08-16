"""Ball"""
 
def main():
    """Ball"""
    num = 0
    heigh = float(input())
    while True:
        heigh = heigh*(0.6)
        if heigh <= 0.01:
            break
        num += 1
    print(num)
main()