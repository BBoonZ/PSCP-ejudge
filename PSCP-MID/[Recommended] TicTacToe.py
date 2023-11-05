"""[Recommended] TicTacToe"""
def main():
    """ XoX """
    board = [input().replace('O', '1').replace('X', '9').replace('-', '0') for _ in range(3)]
    score_3 = score_4 = 0
    for i in range(3):
        score = sum([(int(board[i][j])) for j in range(3)])
        score_2 = sum([(int(board[j][i])) for j in range(3)])
        score_3 += sum([(int(board[i][i]))])
        score_4 += sum([(int(board[i][2-i]))])
        if score == 3 or score_2 == 3 or score_3 == 3 or score_4 == 3:
            return print('O WIN')
        if score == 27 or score_2 == 27 or score_3 == 27 or score_4 == 27:
            return print('X WIN')
    print('DRAW')
main()
