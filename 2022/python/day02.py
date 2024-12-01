data_name = "day"

with open(f"./data/{data_name}02.txt", "r") as file:
    lines = file.read().splitlines()

options = {
    "A": 1,  # Rock
    "B": 2,  # Paper
    "C": 3,  # Scissors
    "X": 1,  # Rock
    "Y": 2,  # Paper
    "Z": 3,  # Scissors
}

outcomes = {
    # Opponent choice: win, draw, loss
    1: (3, 1, 2),
    2: (1, 2, 3),
    3: (2, 3, 1),
}


def get_points_from_outcome(opponent_choice, outcome) -> int:
    outcome -= 1
    return outcomes[opponent_choice][outcome] + (outcome * 3)


def get_outcome(player_choice: int, opponent_choice: int) -> int:
    # 0: loss
    # 3: draw
    # 6: win

    win = 6
    draw = 3
    loss = 0

    if player_choice == opponent_choice:
        return draw

    if (
        (player_choice == 1 and opponent_choice == 3)
        or (player_choice == 2 and opponent_choice == 1)
        or (player_choice == 3 and opponent_choice == 2)
    ):
        return win

    return loss


def get_points(outcome: int, player_choice: int) -> int:
    return outcome + player_choice


total_points = 0

for line in lines:
    # opponent, player = list(map(lambda x: options[x], line.strip().split()))
    # outcome = get_outcome(player, opponent)
    # points = get_points(outcome, player)

    opponent, outcome = list(map(lambda x: options[x], line.strip().split()))
    points = get_points_from_outcome(opponent, outcome)

    total_points += points

print("Total points: ", total_points)
