# def find_sum(n):
#     """Recursively calculate the sum of the first n numbers"""
#     if n == 0:
#         return 0
#     else:
#         return n + find_sum(n - 1)


# print(find_sum(5))


def recursive_power(integer1, integer2):
    if integer2 == 0:
        return 1
    else:
        return integer1 * recursive_power(integer1, integer2 - 1)


print(recursive_power(5, 3))
