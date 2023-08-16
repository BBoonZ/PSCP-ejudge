"""Elo"""
 
def rating(r_a, r_b, player):
    """Elo rating system"""
    if player == 'A':
        return 1 / (1+10**((r_b-r_a)/400))
    return 1 / (1+10**((r_a-r_b)/400))
 
 
def main():
    """Elo"""
    ra_a = int(input())
    ra_b = int(input())
    player = str(input())
 
    test = rating(ra_a, ra_b, player)
    print("%.2f"% round(test, 2))
main()