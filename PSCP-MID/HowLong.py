"""BootSequence"""
def main():
    """บังเอิญช่วงนี้มีบางคนให้ต้องคิดถึงไง ก็โปรดเข้าใจคนมีความรักก็เป็นอย่างงี้"""
    val = abs(int(input()))
    nub = 0
    while True:
        if val == 0:
            nub += 1
        if val < 1:
            break
        val /= 10
        nub += 1
    print(nub)
main()