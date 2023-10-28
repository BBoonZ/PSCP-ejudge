"""[Recommended] RunGame"""
def main(item, dis=0):
    last_dis = 0
    for i in item:
        dis += abs(last_dis-int(i))
        last_dis = int(i)
    print(dis)
main(input().split())
