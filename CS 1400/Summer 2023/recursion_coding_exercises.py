# -----------------------------------------------------------------------------
# problem 1
# -----------------------------------------------------------------------------


def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)


print(recursive_sum(5))

# -----------------------------------------------------------------------------
# problem 2
# -----------------------------------------------------------------------------


def list_sum(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + list_sum(numbers[1:])


print(list_sum([1, 2, 3, 4, 5]))

# -----------------------------------------------------------------------------
# problem 3
# -----------------------------------------------------------------------------


def bunny_ears(bunnies):
    if bunnies == 0:
        return 0
    else:
        return 2 + bunny_ears(bunnies - 1)


print(bunny_ears(1))

# -----------------------------------------------------------------------------
# problem 4
# -----------------------------------------------------------------------------


def reverse_string(input_string):
    if len(input_string) == 0:
        return ""
    else:
        return input_string[-1] + reverse_string(input_string[:-1])


print(reverse_string("cat"))

# -----------------------------------------------------------------------------
# problem 5
# -----------------------------------------------------------------------------


def get_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        max_rest = get_max(numbers[1:])
        return numbers[0] if numbers[0] > max_rest else max_rest


print(get_max([11, 22, 3, 41, 15]))
