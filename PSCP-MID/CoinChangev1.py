"""CoinChangev1"""
def main(baht, coin=0):
    """money rain"""
    coin += baht//25
    coin += (baht%25)//10
    coin += (baht%25%10)//5
    coin += (baht%25%10%5)
    print(coin)
main(int(input()))
