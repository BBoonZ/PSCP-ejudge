"""LAB2"""
def main():
    """Pep8"""
    val = []
    check = 0
    val.append(float(input()))
    val.append(float(input()))
    val.append(float(input()))
    val2 = val.copy()
    for i in val:
        if check < i:
            check = i
            val2.remove(check)
            val2.append(check)
    val_sum = val2[0]**2+val2[1]**2
    if abs(val_sum-val2[2]**2) <= 0.01:
        print("Yes")
    else:
        print("No")
main()