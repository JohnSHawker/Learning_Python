from csv import DictReader


mlb_data = "student_folder/.exercises/mlb_data.csv"

def best_team(file):
    with open(file, "r") as input_file:
        reader = DictReader(input_file)
        most_wins = 0
        most_wins_row = None
        for row in reader:
            row_wins = int(row["W"])
            print(row)
            if row_wins >= most_wins:
                most_wins = row_wins
                most_wins_row = row
        return most_wins_row["Tm"]

print(best_team("mlb_data.csv"))
