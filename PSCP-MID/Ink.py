"""Ink"""
import math
def main():
    """Ink or Drink"""
    val = input().split()
    location = [input().split() for _ in range(int(val[1]))]
    val = int(val[0])
    for i in location:
        radius_house = (int(i[0])**2+int(i[1])**2)**0.5
        print(math.ceil((radius_house**2*3.1416)/val))
main()
