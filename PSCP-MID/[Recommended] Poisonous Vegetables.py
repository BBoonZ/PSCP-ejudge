"""[Recommended] Poisonous Vegetables"""
import json
def main(area, max_area, day):
    """ผักที่ขม คือขนตติดที่คอ"""
    plant_list = []
    out_list = []
    for _ in range(int(area[:area.find('x')])):
        txt = input()
        txt = txt.replace(' ', ', ')
        txt = txt.replace('][', '], [')
        plant_list.extend(json.loads('[' + txt + ']'))
    for i in plant_list:
        if int(i[1]) > max_area:
            out_list.append('[ - ]')
        elif int(i[0]) - int(i[2]) == 0 and int(i[0]) <= day:
            out_list.append('[ o ]')
        else:
            out_list.append('[ x ]')
    for i in range(len(out_list)):
        if i%int(area[area.find('x')+1:]) == 0 and i != 0:
            print()
        print(out_list[i], end='')
main(input(), int(input()), int(input()))
