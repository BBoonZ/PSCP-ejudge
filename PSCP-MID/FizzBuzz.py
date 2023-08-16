"""FizzBuz"""
def main():
    """a"""
    val = int(input())+1
    for i in range(1, val):
        if not i%15:
            print("FizzBuzz")
        elif not i%3:
            print("Fizz")
        elif not i%5:
            print("Buzz")
        else:
            print(i)
main()