def grid(rows, columns):
    row = 0
    column = 0
    for row in range(rows):
        for column in range(columns):
            print('+', '-', '-', '-', '-', end= ' ')
            column += 1
        print('+')
        print("|", " ", " ", " ", " ", )

grid(rows = int(input("How many rows? ")), columns = int(input("How many columns? ")))