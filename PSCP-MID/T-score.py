"""T-score"""
def main(val_n, val_m):
    """val_m = val_m !!!??? chatchawann~~~"""
    score_list = [int(input()) for _ in range(val_n)]
    x_bar = sum(score_list)/len(score_list)
    ex2 = sum([i for i in score_list])**2
    ex_2 = sum([i**2 for i in score_list])
    sd_val = ((val_n*ex_2-ex2)/(val_n*(val_n-1)))**0.5
    for i in score_list:
        if sd_val != 0:
            z_val = (i-x_bar)/sd_val
        else:
            z_val = 0
        print("%.2f" %(50+(10*z_val)))
    val_m = val_m
main(int(input()), int(input()))
