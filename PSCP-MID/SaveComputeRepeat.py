"""SaveComputeRepeat"""
def main():
    """A"""
    start_here = 492137954293754252786
    miliseconds = start_here
    seconds = miliseconds//1000
    miliseconds = miliseconds%1000
    mins = seconds//60
    seconds = seconds%60
    hours = mins//60
    mins = mins%60
    days = hours//24
    hours = hours%24
 
    print(days, hours, mins, seconds, miliseconds)
main()