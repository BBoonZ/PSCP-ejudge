"""Bonus"""
def main():
    """bonus ข้อนี้เจบจรืง"""
    money = int(input())
    year = int(input())
    month = int(input())
    bonus = 0
    if month >= 10:
        year += 1
    if year <= 20:
        bonus += money*year
    else:
        bonus += money*20

    if bonus > 1000000:
        bonus = 1000000
    if bonus < 5000:
        bonus = 5000
    print(bonus)
main()
