"""[Recommended] WPM"""
def main(age, wpm):
    """WPM i gonna do 60wpm"""
    kid_dict = {
        11 : 'Very Slow',
        21 : 'Slow',
        31 : 'Average',
        41 : 'Fast',
        999 : 'Very Fast'
    }
    adult_dict = {
        26 : 'Very Slow',
        36 : 'Slow/Beginner',
        46 : 'Intermediate/Average',
        66 : 'Fast/Advanced',
        81 : 'Very Fast',
        999 : 'Insane'
    }
    if age == 'Kids':
        for i, j in kid_dict.items():
            if wpm >= i:
                continue
            if i == 999 or True:
                print(j)
                break
    else:
        for i, j in adult_dict.items():
            if wpm >= i:
                continue
            if i == 999 or True:
                print(j)
                break
main(input(), int(input()))
