import json

config = json.loads(open("config.json", "r").read())
width = config["screen_width"]
height = config["screen_width"] // config["aspect_ratio"][0] * config["aspect_ratio"][1]
verbose = config["verbose"]
full_screen = config["full_screen"]