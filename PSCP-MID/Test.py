txt = 'Bom 6bay, German Rex, Manx, Manx'
mlist = []

mlist.extend(txt.split(','))
print(mlist)

txt2 = 'Bom bay'
txt3 = ' Bom bay'
txt4 = ' Bombay'
print(txt2.lstrip())
print(txt3.lstrip())
print(txt4.lstrip())