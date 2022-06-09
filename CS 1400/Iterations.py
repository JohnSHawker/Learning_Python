import math

def mysqrt(a):
    x = float(2)
    while True:
        y = (x + a / x) / 2
        if y == x:
            return y
        return y

def test_square_root():
    print(f"a\t mysqrt\t math.sqrt\t difference")
    print(f"_\t ______\t _________\t __________")
    test_number = float(1)
    while test_number < 11:
        print(f"{test_number}\t {mysqrt(test_number)}\t {math.sqrt(test_number)}\t {abs(mysqrt(test_number) - math.sqrt(test_number))}")
        test_number += 1

test_square_root()