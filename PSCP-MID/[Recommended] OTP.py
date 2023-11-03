"""[Recommended] OTP"""
def main():
    """i love OTP"""
    while True:
        otp_dict, check_2, check_3 = {}, [], []
        otp = input()
        if otp == '0':
            break
        for i in otp:
            otp_dict[i] = otp_dict.get(i, 0) + 1
        for i in otp_dict.values():
            if i == 2:
                check_2.append(i)
            elif i == 3:
                check_3.append(i)
        if len(otp) == 4 and len(check_2) == 1:
            print('Valid')
        elif len(otp) == 6 and (len(check_2) == 2 or len(check_3) == 1):
            print('Valid')
        elif len(otp) == 8 and (len(check_2) == 3 or len(check_3) == 2):
            print('Valid')
        else:
            print('Invalid')
main()
