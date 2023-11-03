"""BreakPassword"""
import hashlib
def main(txt):
    """breakpass breakjai"""
    for i in range(0, 100000):
        check = str(i).zfill(5)
        if (hashlib.sha512(check.encode('utf-8')).hexdigest().upper()) == txt:
            print(check)
            break
main(input())
