import random
import time

from placer import Placer
from local_configuration import local_configuration
from target_configuration import target_configuration
from color import get_color_from_index

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


while True:
    for placer in placers:
        if placer.last_placed + PLACE_INTERVAL + random.randrange(5, 25) > time.time():
            continue

        print("\nAttempting to place for: " + placer.username)

        placer.update_board()
        targetPixel = placer.board.get_mismatched_pixel(target_configuration.get_config()["pixels"])

        if targetPixel is None:
            print("No mismatched pixels found")
            continue

        placer.place_tile(targetPixel["x"], targetPixel["y"], get_color_from_index(targetPixel["color_index"]))

        time.sleep(5)

    time.sleep(5)