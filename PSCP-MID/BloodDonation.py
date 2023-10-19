'''BloodDonation'''
def main():
    """i'm B bro"""
    _age = _weight = _book = False
    _time = _check = True
    age = int(input())
    weight = int(input())
    time = int(input())

    if 17 <= age <= 70:
        _age = True
    if weight >= 45:
        _weight = True
    if time == 0 and age > 55:
        _time = False
    if age == 17 or 60 <= age <= 70:
        _book = (input() == 'True')
        _check = False

    if (_age and _weight and _time and _check) or (_age and _weight and _time and _book):
        print('Yes')
    else:
        print('No')
main()
