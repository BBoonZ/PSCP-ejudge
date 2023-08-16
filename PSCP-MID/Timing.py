"""Timing"""
def main(time):
    """A"""
    seconds = time
    mins = seconds//60
    seconds = seconds%60
    hours = mins//60
    mins = mins%60
    days = hours//24
    hours = hours%24
    print(days, hours, mins, seconds)
main(int(input()))