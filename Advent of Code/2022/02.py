import sys

input_file_path = sys.argv[1]

def score_player_choice(choice):
    match choice:
        case "Rock":
            return 1
        case "Paper":
            return 2
        case "Scissors":
            return 3

def parse_play(char):
    match char:
        case "A":
            return "Rock"
        case "B":
            return "Paper"
        case "C":
            return "Scissors"
        case "X":
            return "Rock"
        case "Y":
            return "Paper"
        case "Z":
            return "Scissors"
def score_outcome(outcome):
    us = parse_play(outcome[2])
    them = parse_play(outcome[0])
    return score_player_choice(us) + score_win(us, them)

def score_win(us, them):
    match (us, them):
        case ("Rock", "Scissors") | ("Paper", "Rock") | ("Scissors", "Paper"):
            return 6
        case ("Scissors", "Rock") | ("Rock", "Paper") | ("Paper", "Scissors"):
            return 0
        case _:
            return 3

def part_one():
    with open(input_file_path, "r") as input_file:
        outcomes = input_file.readlines()
        scores = [score_outcome(outcome) for outcome in outcomes]
        print(sum(scores))

part_one()