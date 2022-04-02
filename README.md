Bot for the r/place event.

Based on code from https://github.com/goatgoose/PlaceBot and https://github.com/rdeepak2002/reddit-place-script-2022.

The script in converter can be used to convert an image to a target configuration. Alpha=255 pixels are ignored.

The bot (run via placebot.py) can be configured using config.json. It logs into multiple accounts and pulls the target config from a server via http every 60 seconds.
Every 5 minutes (+5-25 secs), each account pulls the board and attempts to place a misplaced pixel.