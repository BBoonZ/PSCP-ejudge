"""Gekko"""
def gekko(num):
    """ARKKK"""
    for _ in range(num):
        var_input = int(input())
        temp = var_input
        counter = 2
        trigger = 0
        c_t = []
        n_t = ""
        while True:
            if var_input == 1:
                print("1")
                break
 
            if counter == temp:
                c_t.append(str(counter))
                for i in range(len(c_t)):
                    if n_t == "" and c_t[i] not in n_t:
                        n_t += c_t[i]
                    elif c_t[i] not in n_t and n_t != "":
                        n_t += " x " + c_t[i]
                        trigger = 0
                    if c_t[i] in n_t and trigger != 1 and c_t.count(c_t[i]) > 1:
                        n_t = n_t.replace(c_t[i], str(c_t[i] + "**" + str(c_t.count(c_t[i]))))
                        trigger = 1
                print(n_t)
                break
 
            if temp % counter == 0:
                c_t.append(str(counter))
                temp = temp / counter
                counter = 2
            else:
                counter += 1
 
gekko(int(input()))
