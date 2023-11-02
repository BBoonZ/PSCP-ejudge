"""SqFree"""
def main(num):
    """SqFree"""
    count = num
    for i in range(1, num+1):
        for j in range(2, int(num**0.5)+1):
            if i%j**2 == 0:
                count -= 1
                break
    print(count)
main(int(input()))
