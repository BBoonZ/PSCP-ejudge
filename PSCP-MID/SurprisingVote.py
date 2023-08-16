"""SurprisingVote"""
def main():
    """อย่าเดินวนเหมือนนาฬิกา ให้เดินไปข้างหน้าเหมือนปฎิทิน"""
    val_max = float(input())
    val_high = float(input())
    if val_max-val_high*2 < val_high-2 and val_high > 2:
        return print("Surprising")
    return print("Not surprising")
main()