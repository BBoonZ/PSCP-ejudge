"""RuleofThree"""
def main():
    """ปวดหลังลาน้าา"""
    rob = int(input())
    test = 0
    best_p = 0
    best_m = 0
    for _ in range(rob):
        piece = float(input())
        mass = float(input())
        if mass/piece >= test:
            if test == mass/piece:
                best_p = min(best_p, piece)
                best_m = min(best_m, mass)
                continue
            test = mass/piece
            best_p = piece
            best_m = mass
    print('%.02f %.02f'% (best_p, best_m))
main()
