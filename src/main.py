from data_loader import load_laptops
from scorer import rank_laptops


def get_weights():

    print("\nRate importance (1 = Low, 5 = High)\n")

    weights = {}

    weights["performance"] = int(input("Performance: "))
    weights["battery"] = int(input("Battery: "))
    weights["portability"] = int(input("Portability: "))
    weights["brand"] = int(input("Brand: "))
    weights["ram"] = int(input("RAM: "))

    return weights


def main():

    print("==== Laptop Decision Companion System ====\n")

    laptops = load_laptops()

    budget = int(input("Enter your budget (₹): "))

    weights = get_weights()

    results = rank_laptops(laptops, budget, weights)

    if not results:
        print("\n❌ No laptops found under your budget.")
        return

    print("\n📊 Recommended Laptops:\n")

    for i, l in enumerate(results, 1):

        print(f"{i}. {l.name}")
        print(f"   Brand: {l.brand}")
        print(f"   Price: ₹{l.price}")
        print(f"   RAM: {l.ram} GB | Storage: {l.storage} GB")
        print(f"   Score: {l.score:.2f}\n")


if __name__ == "__main__":
    main()