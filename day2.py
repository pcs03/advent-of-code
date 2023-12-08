import re

with open("./data/day2.txt", "r") as file:
    lines = file.read().strip()

game_sum = 0

for line in lines.split("\n"):
    cube_count = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }
    
    game, sets = line.split(":")

    game = int(re.findall(r'\d+', game)[0])

    for set in sets.split(";"):
        cubes = set.split(",")

        for cube in cubes:
            cube = cube.strip()
            count, color = cube.split(" ")
        
            old_count = cube_count[color]

            if int(count) > old_count:
                cube_count[color] = int(count)
    game_sum += cube_count["red"] * cube_count["green"] * cube_count["blue"]

print(game_sum)
