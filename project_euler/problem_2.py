fibonacci_sequence = [1, 2]
even_fibonacci_numbers = []
while fibonacci_sequence[-1] < 4000000:
    fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
print(fibonacci_sequence)
for i in fibonacci_sequence:
    if i % 2 == 0:
        even_fibonacci_numbers.append(i)
print(even_fibonacci_numbers)
print(sum(even_fibonacci_numbers))
