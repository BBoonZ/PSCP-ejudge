"""Blackjack"""
def main():
    """การรอไพ่ที่ออกไปหมดแล้ว ก็เหมือนรอความรักจากคนไม่มีใจ"""
    rob = int(input())
    total = 0
    card_a = False
    for _ in range(rob):
        card = input()
        if card.isnumeric():
            total += int(card)
        elif not card.isnumeric() and card != 'A':
            total += 10
        elif card == 'A' and total+11 <= 21:
            total += 11
            card_a = True
        else:
            total += 1
    if card_a and total > 21:
        total -= 10
    print(total)
main()

