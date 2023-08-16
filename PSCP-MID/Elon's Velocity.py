"""DAY1"""
def main(meter, time):
    """A"""
    velocity = meter / abs(time)
    print(velocity)
main(float(input()), int(input()))