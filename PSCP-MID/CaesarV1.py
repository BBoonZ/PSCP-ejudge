"""CaesarV1"""
def main(shift, txt, output=''):
    for i in txt:
        if i.isalpha():
            output += chr(ord(i)+shift) if (ord(i)+shift) > 97 else chr((ord(i)+shift)+26)
            print(output, ord(i)+shift)
        else:
            output += i
    print(output)
main(int(input()), input())
