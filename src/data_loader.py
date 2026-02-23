import json
from models import Laptop


def load_laptops():

    with open("data/laptops.json", "r") as file:
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