"""SumOfNumber"""
def main():
    """ตอนนั้นฉันคงเมารักอยู่ (ฉันก็เลยคิด ก็เลยคิด ว่าเธอจริงใจ)"""
    first = int(input())
    val_sum = 0
    while True:
        if val_sum == first:
            break
        val = int(input())
        if val == -1:
            break
        val_sum += val
    print(val_sum)
main()