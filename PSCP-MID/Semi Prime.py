"""Semi Prime"""
def main(num):
    for i in range(num):
        for j in range(2, int(i**0.5)+1):
            if i%j == 0:
                print(i, j, 'min')
                for k in range(j, i+1):
                    if i%k == 0 and j*k == i:
                        print(j, k)
                        for l in range(2, k)
                break
main(int(input()))
