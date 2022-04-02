import random
import time

from PIL import UnidentifiedImageError

from placer import Placer
from local_configuration import local_configuration
from target_configuration import target_configuration
from color import get_color_from_index, Color

# placer = Placer()
# placer.login(local_configuration["accounts"][2]["username"], local_configuration["accounts"][2]["password"])
# placer.update_board()
#
# # placer.place_tile(1955, 3, Color.LIGHT_GREEN)
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

        try:
            placer.update_board()
        except UnidentifiedImageError:
            print("Unidentified image for: " + placer.username)
            print("ABORTING!!!!!!!!!!!!")
            print("ABORTING!!!!!!!!!!!!")
            print("ABORTING!!!!!!!!!!!!")
            continue

        mismatched_pixels = placer.board.get_mismatched_pixels(target_configuration.get_config()["pixels"])
        targetPixel = placer.board.get_mismatched_pixel(target_configuration.get_config()["pixels"])

        if targetPixel is None:
            print("No mismatched pixels found")
            continue

        print("Mismatched pixel found (" + (str(len(mismatched_pixels))) + "/" + (str(len(target_configuration.get_config()["pixels"]))) + "): " + str(targetPixel))
        placer.place_tile(targetPixel["x"], targetPixel["y"], get_color_from_index(targetPixel["color_index"]))
        print()

        time.sleep(5)

    print("ETA:   ", ",  ".join([p.username + " - " + str(round(p.last_placed + PLACE_INTERVAL + 15 - time.time())) + " s" for p in placers]))

    time.sleep(30)


# Traceback (most recent call last):
# File "src/placebot.py", line 52, in <module>
# placer.update_board()
# File "/home/place/place/src/placer.py", line 162, in update_board
# self.update_canvas(1)
# File "/home/place/place/src/placer.py", line 223, in update_canvas
# temp = json.loads(ws.recv())
# File "/home/place/place/.venv/lib/python3.8/site-packages/websocket/_core.py", line 357, in recv
# opcode, data = self.recv_data()
# File "/home/place/place/.venv/lib/python3.8/site-packages/websocket/_core.py", line 380, in recv_data
# opcode, frame = self.recv_data_frame(control_frame)
# File "/home/place/place/.venv/lib/python3.8/site-packages/websocket/_core.py", line 401, in recv_data_frame
# frame = self.recv_frame()
# File "/home/place/place/.venv/lib/python3.8/site-packages/websocket/_core.py", line 440, in recv_frame
# return self.frame_buffer.recv_frame()
# File "/home/place/place/.venv/lib/python3.8/site-packages/websocket/_abnf.py", line 338, in recv_frame
# self.recv_header()
# File "/home/place/place/.venv/lib/python3.8/site-packages/websocket/_abnf.py", line 294, in recv_header
# header = self.recv_strict(2)
# File "/home/place/place/.venv/lib/python3.8/site-packages/websocket/_abnf.py", line 373, in recv_strict
# bytes_ = self.recv(min(16384, shortage))
# File "/home/place/place/.venv/lib/python3.8/site-packages/websocket/_core.py", line 524, in _recv
# return recv(self.sock, bufsize)
# File "/home/place/place/.venv/lib/python3.8/site-packages/websocket/_socket.py", line 122, in recv
# raise WebSocketConnectionClosedException(
#     websocket._exceptions.WebSocketConnectionClosedException: Connection to remote host was lost.