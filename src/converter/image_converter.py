import json

from PIL import Image
import sys

from src.color import get_closest_color

if len(sys.argv) < 4:
    print("Usage: python3 image_converter.py <input_image> <offset_x> <offset_y>")
    exit(1)

offset_x = int(sys.argv[2])
offset_y = int(sys.argv[3])

image_filename = sys.argv[1]
print("Reading image: " + image_filename)
image = Image.open(image_filename)
image_data = image.load()

print("Converting image...")
target_pixels = []

for x in range(image.width):
    for y in range(image.height):
        rgba = image_data[x, y]

        if(rgba[3] == 0):  # skip transparent pixels
            continue

        closest_color = get_closest_color(rgba[0], rgba[1], rgba[2])

        target_pixels.append({
            "x": x + offset_x,
            "y": y + offset_y,
            "color_index": closest_color.value["id"]
        })

print("Writing out.cfg ...")
with open("out.cfg", "w") as target_file:
    json.dump({
        "pixels": target_pixels
    }, target_file)

print("Done!")