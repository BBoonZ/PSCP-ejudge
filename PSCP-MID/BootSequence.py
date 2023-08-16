"""BootSequence"""
def main():
    """ถ้าฉันทักไปคงดี ถ้าบอกว่าชอบไปคงดี ถ้าเรารักกันคงดี สุดท้ายฉันยอมแพ้อยู่ดี"""
    val = int(input())
    for i in range(1, val):
        print(i, end="_")
    print(val)
main()