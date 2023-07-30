values = ((14, 5), (9, 8), (144, 983), (7000, 1), (54, 54))

def num_digits(num):
    return len(str(num))

def num_digits_in_tuple(tuple):
    accumulator = 0
    for num in tuple:
        accumulator += num_digits(num)
    return accumulator

def sort_values(values):
    return tuple(sorted(values, key = num_digits_in_tuple))

print(sort_values(values))

# _____________________________________________________________________________

student_grades = (('MaKayden', 82), ('Nyron', 'N/A'), ('Taylor', 80), ('Noel', 'N/A'))

def remove_NA(student_grades):
    output = []
    for student in student_grades:
        grade = 'Test not taken yet' if student[1] == 'N/A' else student[1]
        info = (student[0], grade)
        output.append(info)
    return tuple(output)

print(remove_NA(student_grades))

# _____________________________________________________________________________

dividend = (10, 100, 1000, 10000)
divisor = (5, 50, 500, 5000)

def find_quotient(dividends, divisors):
    quotient_output = []
    for dividend, divisor in zip(dividends, divisors):
        quotient = dividend / divisor
        quotient_output.append(quotient)
    return tuple(quotient_output)

print(find_quotient(dividend, divisor))

# _____________________________________________________________________________

numbers = (8, 5, 9, 14, 22)

def find_adj_products(numbers):
    output_product = []
    for i in range(len(numbers) - 1):
        product = numbers[i] * numbers[i + 1]
        output_product.append(product)
    return tuple(output_product)

print(find_adj_products(numbers))

# _____________________________________________________________________________

tuple_pairs = ((4, 5), (6, 14), (100, 40), (0, 83))

def find_pair_diff(pairs):
    diff = []
    for nums in pairs:
        diff.append(abs(nums[0] - nums[1]))
    return tuple(diff)

def find_max_diff(pairs):
    diff = find_pair_diff(pairs)
    max_diff = max(diff)
    index_of_max_diff = diff.index(max_diff)
    return (pairs[index_of_max_diff], max_diff)

print(find_pair_diff(tuple_pairs))
print(find_max_diff(tuple_pairs))