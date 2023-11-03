"""Gram_v1"""
def main(txt):
    """i think have some one wrong"""
    gram_dict = {}
    for i in range(len(txt)):
        gram_dict[txt[i:i+2]] = gram_dict.get(txt[i:i+2], 0) + 1
    gram_dict = dict(sorted(gram_dict.items(), key=lambda x: x[1], reverse=True))
    print(*list(gram_dict.items())[0], sep='\n')
main(input())
