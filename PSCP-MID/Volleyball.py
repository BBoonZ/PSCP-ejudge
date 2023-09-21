"""Volleyball"""
def main():
    text = input()
    team_a = 0
    team_b = 0
    score_a = 0
    score_b = 0
    output = ''
    set = 1
    for i in text:
        if i == 'A':
            team_a += 1
        else:
            team_b += 1
        if (team_a >= 25 or team_b >= 25) and abs(team_a-team_b) >= 2:
            output += 'Set ' + str(set) + ': A (' + str(team_a) + ') | B (' + str(team_b) + ')\n'
            if team_a > team_b:
                score_a += 1
            else:
                score_b += 1
            team_a = team_b = 0
            set += 1

    if team_a >= 0 and team_b >= 0 and set != 5:
        output += 'Set ' + str(set) + ': A (' + str(team_a) + ') | B (' + str(team_b) + ')\n'

    if set == 5 or (set == 4 and (score_a == 3 or score_b ==3)):
        if score_a > score_b:
            output += 'A won ' + str(score_a) + ':' + str(score_b) + ' set'
        else:
            output += 'B won ' + str(score_b) + ':' + str(score_a) + ' set'
    else:
        output += 'The game has not finished yet.'
    print(output)
main()