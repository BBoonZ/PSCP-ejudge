"""LAB2"""
def find(val2, i):
    """ดูมาจ้าาา"""
    val = int(input())
    i += 1
    if val > val2:
        val2 = val
    if i == 8:
        print(val2)
        return
    find(val2, i)
 
def main():
    """เพื่อนช่วยจ้าาาา"""
    find(int(input()), 1)
main()