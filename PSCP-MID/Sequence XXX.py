"""Sequence XXX"""
def main():
    """ได้แต่คอย คอย คอย
        ได้แต่คอย คอย คอย"""
    val_n = int(input())
    val_m = int(input())
    final = ''
    for i in range(val_n):
        output = ''
        for j in range(val_n):
            if i == j or i+j == val_n-1 or i == 0 or j == 0 or i == val_n-1 or j == val_n-1:
                output += '*'
            else:
                output += ' '
        final += (output+' ')*val_m + '\n'
    print(final)
main()
