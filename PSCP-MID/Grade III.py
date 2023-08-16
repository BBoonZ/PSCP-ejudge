"""Grade III"""
def main():
    """ลา ลา ลา~~~"""
    rob = int(input())
    val_sum = 0
    for i in range(rob):
        i = float(input())
        if i >= 95 and i <= 100:
            val_sum += 4
        elif i >= 90:
            val_sum += 3.5
        elif i >= 85:
            val_sum += 3
        elif i >= 80:
            val_sum += 2.5
        elif i >= 75:
            val_sum += 2
        elif i >= 70:
            val_sum += 1.5
        elif i >= 65:
            val_sum += 1
        elif i >= 60:
            val_sum += 0.5
        elif i >= 0:
            val_sum += 0
    print("%.2f"% abs(val_sum/rob-0.005))
main()