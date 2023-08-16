"""Nearer"""
def main():
    """Nearer"""
    alice = int(input())
    bob = int(input())
    icetim = int(input())
    if abs(icetim-alice) < abs(icetim-bob):
        print("Alice %d" %abs(icetim-alice))
    elif abs(icetim-alice) > abs(icetim-bob):
        print("Bob %d" %abs(icetim-bob))
    else:
        print("Sundaes %d" %abs(icetim-bob))
main()