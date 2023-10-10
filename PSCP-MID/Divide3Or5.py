"""Divide3Or5"""
def main():
    """ddd"""
    val = int(input())
    count = 0
    for i in range(1, val+1):
        if i%3 == 0 or i%5 == 0:
            count += i
    print(count)
main()
