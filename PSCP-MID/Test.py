val_1 = input()
val_2 = input()
val_3 = input()

my_list = []
my_list.append(val_1+val_2+val_3)
my_list.append(val_1+val_3+val_2)
my_list.append(val_2+val_1+val_3)
my_list.append(val_2+val_3+val_1)
my_list.append(val_3+val_1+val_2)
my_list.append(val_3+val_2+val_1)

print(my_list)