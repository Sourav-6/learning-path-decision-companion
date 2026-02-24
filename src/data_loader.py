import json
import os
from models import Laptop


def load_laptops():

    # Get project root directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Build correct path to data file
    data_path = os.path.join(base_dir, "data", "laptops.json")

    # Load JSON
    with open(data_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    laptops = []

    for item in data:

        laptop = Laptop(
            item["name"],
            item["brand"],
            item["price"],
            item["ram"],
            item["storage"],
            item["cpu_score"],
            item["battery"],
            item["weight"],
            item["brand_score"]
        )

        laptops.append(laptop)

    return laptops