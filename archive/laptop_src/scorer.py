def calculate_score(laptop, weights):

    performance = laptop.cpu_score * weights["performance"]
    battery = laptop.battery * weights["battery"]
    portability = (10 - laptop.weight) * weights["portability"]
    brand = laptop.brand_score * weights["brand"]
    ram = laptop.ram / 2 * weights["ram"]

    total = (
        performance +
        battery +
        portability +
        brand +
        ram
    )

    return total


def rank_laptops(laptops, budget, weights):

    valid = []

    for laptop in laptops:
        if laptop.price <= budget:
            valid.append(laptop)

    for laptop in valid:
        laptop.score = calculate_score(laptop, weights)

    valid.sort(key=lambda x: x.score, reverse=True)

    return valid