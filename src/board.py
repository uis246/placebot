import random
import time

from PIL import Image

from color import get_matching_color, Color

BOARD_SIZE_X = 1000
BOARD_SIZE_Y = 1000

class Board:

    def __init__(self):
        self.last_update = 0
        self.colors = None

    def update_image(self, raw_image):
        self.last_update = time.time()

        image = Image.open(raw_image).convert("RGB").load()

        self.colors = []

        # convert to color indices
        for x in range(BOARD_SIZE_X):
            column = []
            for y in range(BOARD_SIZE_Y):
                column.append(get_matching_color(image[x, y]))
            self.colors.append(column)

        print("Board updated.")
    
    def get_pixel_color(self, x: int, y: int) -> Color:
        return self.colors[x][y]

    def get_mismatched_pixel(self, target_pixels):
        mismatched_pixels = self.get_mismatched_pixels(target_pixels)

        if len(mismatched_pixels) == 0:
            return None

        return random.choice(mismatched_pixels) # TODO: does this work?

    def get_mismatched_pixels(self, target_pixels):
        mismatched_pixels = []
        for target_pixel in target_pixels:
            currentColor = self.get_pixel_color(target_pixel["x"], target_pixel["y"])
            if currentColor.value["id"] != target_pixel["color_index"]:
                mismatched_pixels.append(target_pixel)
        return mismatched_pixels