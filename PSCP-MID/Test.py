val_f = 120
area = {150 : 5000, 250 : 6000}
total = 0
for i in area.keys():
    if val_f > i:
        continue
    total += area.get(i)
    break
print(total)