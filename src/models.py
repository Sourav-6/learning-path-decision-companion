class Laptop:

    def __init__(
        self,
        name,
        brand,
        price,
        ram,
        storage,
        cpu_score,
        battery,
        weight,
        brand_score
    ):

        self.name = name
        self.brand = brand
        self.price = price
        self.ram = ram
        self.storage = storage
        self.cpu_score = cpu_score
        self.battery = battery
        self.weight = weight
        self.brand_score = brand_score

        self.score = 0