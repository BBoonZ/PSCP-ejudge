"""Volleyball"""
def main():
    """wow i it did"""
    text = input()
    team_a = 0
    team_b = 0
    score_a = 0
    score_b = 0
    output = ''
    rob = 1
    for i in text:
        if i == 'A':
            team_a += 1
        else:
            team_b += 1
        if (team_a >= 25 or team_b >= 25) and abs(team_a-team_b) >= 2 or \
            ((team_a >= 15 or team_b >= 15) and abs(team_a-team_b) >= 2 and rob == 5):
            output += 'Set ' + str(rob) + ': A (' + str(team_a) + ') | B (' + str(team_b) + ')\n'
            if team_a > team_b:
                score_a += 1
            else:
                score_b += 1
            team_a = team_b = 0
            rob += 1

    if team_a >= 0 and team_b >= 0 and rob != 6 and (score_a < 3 and score_b < 3):
        output += 'Set ' + str(rob) + ': A (' + str(team_a) + ') | B (' + str(team_b) + ')\n'

    if rob == 6 or (score_a >= 3 or score_b >= 3):
        if score_a > score_b:
            output += 'A won ' + str(score_a) + ':' + str(score_b) + ' set'
        else:
            output += 'B won ' + str(score_b) + ':' + str(score_a) + ' set'
    else:
        output += 'The game has not finished yet.'
    print(output)
main()
