"""Diamond I"""
def main():
    """เพชรจริงต้อง y <= 0"""
    val_i = int(input())
    val_j = int(input())
    m_list = []
    s_list = []
    for i in range(val_i):
        m_list.extend(input().split())
    for i in range(val_j):
        total = 0
        for j in range(i, val_i*val_j, val_j):
            total += int(m_list[j])
        s_list.append(total)
    s_list.sort()
    print(s_list[-1])
main()
