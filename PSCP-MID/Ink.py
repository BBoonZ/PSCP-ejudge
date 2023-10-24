"""Ink"""
def main():
    """Ink or Drink"""
    val = input().split()
    location = [input().split() for _ in range(int(val[1]))]
    val = int(val[0])
    for i in location:
        radius_house = (int(i[0])**2+int(i[1])**2)**0.5
        ink_radius = time = ink = 0
        while True:
            if ink_radius >= radius_house:
                break
            ink += val
            ink_radius = (ink/3.1416)**0.5
            time += 1
        print(time)
main()
