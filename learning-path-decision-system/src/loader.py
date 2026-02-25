import json
import os


def load_paths():

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(base_dir, "data", "paths.json")

    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data