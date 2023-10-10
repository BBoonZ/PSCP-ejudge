"""PongYa"""
def main():
    """ping pong pang peww"""
    val = int(input())
    if val % 3 == 0 or str(val)[-1] == '3':
        print('PONG')
    else:
        print(val)
main()
