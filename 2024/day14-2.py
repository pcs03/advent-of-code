import math
from PIL import Image, ImageDraw, ImageFont

def save_grid_as_image(grid, filepath, font_path="/usr/share/fonts/noto/NotoSans-Medium.ttf", font_size=30, cell_size=40):
    """
    Save a grid of characters as an image.
    
    Args:
        grid (list of list of str): 2D list of characters to display in the grid.
        filepath (str): Path to save the generated image.
        font_path (str): Path to the TTF font file. Defaults to DejaVuSans-Bold.
        font_size (int): Font size for characters. Defaults to 30.
        cell_size (int): Size of each cell in pixels. Defaults to 40.
    """
    # Calculate image dimensions
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    image_width = cols * cell_size
    image_height = rows * cell_size

    # Create a blank image
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    # Load the font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except OSError:
        print("Font not found. Using default font.")
        font = ImageFont.load_default()

    # Draw the characters onto the image
    for row_idx, row in enumerate(grid):
        for col_idx, char in enumerate(row):
            x = col_idx * cell_size + cell_size // 4
            y = row_idx * cell_size + cell_size // 4
            draw.text((x, y), char, font=font, fill="black")

    # Save the image
    image.save(filepath)

with open("./data/day14.txt") as file:
    lines = file.read().splitlines()

# Test
# grid_rows = 7
# grid_cols = 11

# Actual input
grid_rows = 103
grid_cols = 101


def get_future_position(row: int, col: int, d_row: int, d_col: int, seconds: int) -> tuple[int, int]:
    future_col = (col + seconds * d_col) % grid_cols
    future_row = (row + seconds * d_row) % grid_rows

    return future_col, future_row


for i in [*range(2824, 20000, 103), *range(2997, 20000, 101)]:
    future_positions: set[tuple[int, int]] = set()
    print("Seconds: ", i)
    for line in lines:
        pos_string, vel_string = line.split(" ")
        col, row = map(int, pos_string[2:].split(","))
        d_col, d_row = map(int, vel_string[2:].split(","))

        future_position = get_future_position(row, col, d_row, d_col, i)
        future_positions.add(future_position)

    grid: list[list[str]] = []

    for row in range(grid_rows):
        gridline: list[str] = []
        for col in range(grid_cols):
            if (col, row) in future_positions:
                gridline.append("#")
            else:
                gridline.append(" ")
        grid.append(gridline)

    save_grid_as_image(grid, f"~/Downloads/images/grid{i}.png")

