"""Point Sorting"""
def main():
    val_t = int(input())
    output = []
    pigus = []
    pigus_s = []
    for i in range(val_t):
        val_n = int(input())
        for j in range(val_n):
            txt = input()
            pigus.append(txt)
            pigus_s.append(int(txt[:txt.find(' ')])+int(txt[txt.find(' ')+1:]))
    print(pigus)
    print(pigus_s)
main()
