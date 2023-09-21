"""Home Run"""
def main():
    """RUN RUN RUN!!"""
    val_r = int(input())
    tee = float(input())
    count = 0
    for _ in range(val_r):
        tee2 = float(input())
        if tee2 < tee:
            count += 1
    print(count)
main()
