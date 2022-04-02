import json

local_configuration = {}

with open('config.json', 'r') as f:
    local_configuration = json.load(f)