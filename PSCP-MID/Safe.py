"""Safe"""
def main(_pass1, _pass2):
    """how to one line??"""
    print(sum([min(abs(ord(_pass1[i]) - ord(_pass2[i])), \
    abs(abs(ord(_pass1[i]) - ord(_pass2[i])) - 26)) for i in range(len(_pass1))]))
main(input(), input())
