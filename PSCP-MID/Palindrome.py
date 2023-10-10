"""Palindrome"""
def main():
    val_n = 3
    time = '9:19'
    hour = int(time[:time.find(':')])
    sec = int(time[-2])
    for _ in range(val_n):
        if sec%6 == 0 and sec != 0:
            hour += 1
            sec = 0
        if hour%24 == 0 and hour != 0:
            hour = 0
            sec = 0
        output = (str(hour) + ':' + str(sec) + str(hour))
        sec += 1


        print(output)
main()
