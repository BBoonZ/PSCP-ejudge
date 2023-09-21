""""WordSequence II"""
def main():
    """:p"""
    txt = input()
    txt2 = input()
    for i in range(max(len(txt), len(txt2))+1):
        print(txt2[:i] + txt[i:])
main()
