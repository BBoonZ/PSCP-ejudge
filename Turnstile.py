"""Turnstile"""
def main():
    """Turnstile"""
    people = 0
    locked = False
    while True:
        insert = str(input())
        if insert == 'END':
            break
 
        if insert == 'C':
            locked = True
        if insert == 'P' and locked:
            people += 1
            locked = False
    print(people)
main()