import random
import time

from placer import Placer
from local_configuration import local_configuration
from target_configuration import target_configuration
from color import get_color_from_index



# placer = Placer()
# placer.login(local_configuration["accounts"][0]["username"], local_configuration["accounts"][0]["password"])
# placer.update_board()
#
# pixels = placer.board.get_mismatched_pixels(target_configuration.get_config()["pixels"])
#
# for pixel in pixels:
#     print(pixel, " , ", placer.board.get_pixel_color(pixel["x"], pixel["y"]))
#
# exit(0)



PLACE_INTERVAL = 5 * 60

placers = []
for account in local_configuration["accounts"]:
    placer = Placer()
    placer.login(account["username"], account["password"])

    if not placer.logged_in:
        print("Failed to login to account: " + account["username"])
        continue

    placers.append(placer)

print("\n", len(placers), " accounts logged in\n")


counter = 0

while True:
    for placer in placers:
        if placer.last_placed + PLACE_INTERVAL + random.randrange(5, 25) > time.time():
            continue

        print("Attempting to place for: " + placer.username)

        placer.update_board()
        targetPixel = placer.board.get_mismatched_pixel(target_configuration.get_config()["pixels"])

        if targetPixel is None:
            print("No mismatched pixels found")
            continue

        print("Mismatched pixel found: " + str(targetPixel))
        placer.place_tile(targetPixel["x"], targetPixel["y"], get_color_from_index(targetPixel["color_index"]))
        print()

        time.sleep(5)

    counter -= 1
    if counter <= 0:
        counter = 6
        print("ETA:   ", ",  ".join([p.username + " - " + str(round(p.last_placed + PLACE_INTERVAL + 15 - time.time())) + " s" for p in placers]))

    time.sleep(5)