# This solution hashes any hand value + individual character values to a hex number
# Ranks the hands based on this hex number and then calculates the total winnings

card_values = {
    "A": "C",
    "K": "B",
    "Q": "A",
    "T": "9",
    "9": "8",
    "8": "7",
    "7": "6",
    "6": "5",
    "5": "4",
    "4": "3",
    "3": "2",
    "2": "1",
    "J": "0",
}


def get_hand_value(hand) -> str:
    counts = []
    for char, _ in card_values.items():
        counts.append(hand.count(char))

    if counts[-1] == 0:
        counts = sorted(counts, reverse=True)

        if counts[0] == 5:
            return "6"
        elif counts[0] == 4:
            return "5"
        elif counts[0] == 3 and counts[1] == 2:
            return "4"
        elif counts[0] == 3:
            return "3"
        elif counts[0] == 2 and counts[1] == 2:
            return "2"
        elif counts[0] == 2:
            return "1"
        else:
            return "0"
    else:
        j = counts.pop()
        counts = sorted(counts, reverse=True)

        if j > 0:
            if counts[0] + j == 5:
                return "6"
            elif counts[0] + j == 4:
                return "5"
            elif counts[0] + counts[1] + j == 5:
                return "4"
            elif counts[0] + j == 3:
                return "3"
            elif counts[0] + j == 2:
                return "1"
            else:
                raise ValueError("This value shouln't be possible")
    raise ValueError("No hand value was calculated")


def hash_strength(hand) -> int:
    hand_value = get_hand_value(hand)
    hex_string = hand_value

    for char in hand:
        hex_string += card_values[char]
    decimal_value = int(hex_string, 16)

    return decimal_value


with open("./data/day7.txt", "r") as file:
    lines = file.read().splitlines()
    lines = [(line.split()) for line in lines]

cards = []

for hand, bid in lines:
    strength = hash_strength(hand)
    cards.append((strength, hand, int(bid)))
cards = sorted(cards)

total_winnings = 0

for i, card in enumerate(cards):
    total_winnings += (i + 1) * card[2]
print(total_winnings)
