txt = [5, 2, 3, [7, [10, [12, 11], 9], 20], 4]

print(isinstance(txt, (str, float, int)))

print(len(txt))

x = txt[3].copy()

print(x)