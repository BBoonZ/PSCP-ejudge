"""BTU"""
def main():
    """ความรักก็เหมือนแอร์ กอมาลาสแปร์"""
    val_f = int(input())
    height = int(input())
    people = int(input())
    room_type = (input() == 'kitchen')*4000
    room_type2 = input()
    total = 0
    area = {150 : 5000, 250 : 6000, 300 : 7000, 350 : 8000, 400 : 9000, 450 : \
    10000, 550 : 12000, 700 : 14000, 1000 : 18000, 1200 : 21000, 1400 : 23000, \
    1500 : 24000, 2000 : 30000, 2500 : 34000}
    for i in area.keys():
        if val_f > i:
            continue
        total += area.get(i)
        break
    if height > 8:
        total += (height-8)*1000
    if people > 2:
        total += (people-2)*600
    total += room_type
    total += (room_type2 == 'facing the sun')*(total//10)
    total -= (room_type2 == 'shaded')*(total//10)
    print(total)
main()
