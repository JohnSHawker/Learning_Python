import sys

def largest_prime_factor(number):
    i = 2  # Starting factor

    while i * i <= number:
        if number % i == 0:
            number = number / i
        else:
            i += 1

    return int(number)

number = int(sys.argv[1])
# number = 600851475143
largest_factor = largest_prime_factor(number)

print("Largest prime factor of", number, "is:", largest_factor)
