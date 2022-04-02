import json
import time

import requests

from local_configuration import local_configuration

UPDATE_INTERVAL = 60

class TargetConfiguration:
    def __init__(self):
        self.last_update = 0
        self.config = {}

    def get_config(self):
        if self.last_update + UPDATE_INTERVAL < time.time():
            self.refresh_config()
            self.last_update = time.time()

        return self.config

    def refresh_config(self):
        print("\nRefreshing target configuration...\n")

        url = local_configuration["target_configuration_url"]

        if url.startswith("http"):
            r = requests.get(url)

            if r.status_code != 200:
                print("Error: Could not get config file from " + local_configuration["target_configuration_url"])
                return

            # parse config file
            self.config = json.loads(r.text)
        else:
            # not a remote url, fallback to local file
            with open(url, "r") as f:
                self.config = json.load(f)

target_configuration = TargetConfiguration()