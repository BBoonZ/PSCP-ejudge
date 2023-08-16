"""Boomerang"""
def main(var_x, var_y, var_z):
    """A"""
    print(var_x+1)
    print(7*var_y**3+2*var_y**2-31*var_y+1)
    print(-1*var_z)
    print((var_x+var_y)*(var_x-var_y))
    print((var_y-(var_y**2-4*var_x*var_z)**0.5)/(2*var_x))
main(int(input()), int(input()), int(input()))