with open("./data/day15.txt", "r") as file:
    input = file.read().strip().split(",")


def hash_string(string: str) -> int:
    current_value = 0
    for char in string:
        value = ord(char)
        current_value += value
        current_value *= 17
        current_value %= 256
    return current_value


def main():
    boxes = {i: ([], []) for i in range(256)}
    for seq in input:
        if "=" in seq:
            label, focal_length = seq.split("=")
            label_hash = hash_string(label)
            box = boxes[label_hash]

            if label in box[0]:
                label_idxs = [i for i, box_label in enumerate(
                    box[0]) if box_label == label]
                for idx in label_idxs:
                    box[1][idx] = focal_length
            else:
                box[0].append(label)
                box[1].append(focal_length)
        elif "-" in seq:
            label = seq.replace("-", "")
            label_hash = hash_string(label)
            box = boxes[label_hash]

            label_idxs = [i for i, box_label in enumerate(
                box[0]) if box_label == label]
            for idx in label_idxs:
                box[0].pop(idx)
                box[1].pop(idx)
    focal_power = 0
    for box_nr, box in boxes.items():
        lens_sum = 0
        for i, focal_length in enumerate(box[1]):
            lens_sum += (box_nr + 1) * (i + 1) * int(focal_length)
        focal_power += lens_sum
    print(focal_power)


if __name__ == "__main__":
    main()
