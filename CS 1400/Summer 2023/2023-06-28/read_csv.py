import sys
import csv

csv_path = sys.argv[1]

totals = []

with open(csv_path, "r") as input_file:
    reader = csv.DictReader(input_file)
    # print(reader)
    # print(dir(reader))
    # print(reader.fieldnames)
    # print(reader["first"])
    totals = [0 for _ in range(0, len(reader.fieldnames))]
    num_rows = 0
    for row in reader:
        num_rows += 1
        for i, fieldname in enumerate(reader.fieldnames):
            totals[i] += int(row[fieldname])

    # avgs = [total / num_rows for total in totals]
    for i in range(len(totals)):
        totals[i] /= num_rows

    print(totals)
    # print(avgs)