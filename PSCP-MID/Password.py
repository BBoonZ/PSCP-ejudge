"""Password"""
import hashlib
def main(txt):
    """password passjai"""
    print(hashlib.sha512(txt.encode('utf-8')).hexdigest().upper())
main(input())
