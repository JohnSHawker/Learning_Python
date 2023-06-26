import sys

test_file_path = sys.argv[1]

def part_one():
    with open(test_file_path, "r") as file:
        s = file.read().strip()
        elves = s.split("\n\n")
        totals = []
        for elf in elves:
            foods = elf.split("\n")
            total_calories = 0
            for food in foods:
                food = int(food)
                total_calories += food
            totals.append(total_calories)
        return max(totals)
    # print(max(totals))


def part_two():
    with open(test_file_path, "r") as file:
        s = file.read().strip()
        elves = s.split("\n\n")
        totals = []
        for elf in elves:
            foods = elf.split("\n")
            total_calories = 0
            for food in foods:
                food = int(food)
                total_calories += food
            totals.append(total_calories)
        totals.sort()
        totals.reverse()
            # totals.sort(reverse=True)
        print(totals)
        # return max(totals)
        return(sum(totals[0:3]))
    # print(max(totals))

def parse(test_file_path):
    with open(test_file_path, "r") as file:
        s = file.read().strip()
        elves = s.split("\n\n")
        calorieses = []
        for elf in elves:
            foods = elf.split("\n")
            calories = [int(food) for food in foods]
            calorieses.append(calories)
        return calorieses

def part_two_part_two():
    calorieses = parse(test_file_path)
    per_elf_totals = [sum(calories) for calories in calorieses]
    per_elf_totals.sort(reverse = True)
    return sum(per_elf_totals[:3])

print(part_two_part_two())
