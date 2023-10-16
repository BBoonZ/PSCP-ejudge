txt = input()
txt = (txt.replace(i, ' ') for i in txt if i.isalpha())
print(txt)