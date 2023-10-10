"""PrasomSib"""
def main():
    """a 10 20 30 40 a 10 20 30 40"""
    val = input()
    count = 0
    for i in range(len(val)):
        total = int(val[i])
        for j in range(i+1, len(val)):
            total += int(val[j])
            if total == 10:
                count += 1
                break
            elif total > 10:
                break
    print(count)
main()
