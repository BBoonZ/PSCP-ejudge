"""Username"""
def main():
    """เธอมาทำให้ละลาย โดนสาปให้ตายแล้วตายอีก"""
    val = input()
    if val.isnumeric():
        print("Number")
    elif val.isupper():
        print("Uppercase")
    elif val.islower():
        print("Lowercase")
    elif val.istitle():
        print("Title")
    elif val.isspace():
        print("Space")
    else:
        print("Other")
main()