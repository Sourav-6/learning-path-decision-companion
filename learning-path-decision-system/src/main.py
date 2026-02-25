from loader import load_paths
from scorer import rank_paths
from explainer import explain


def get_profile():

    print("\n--- Your Profile ---")

    level = int(input("Your level (1=Beginner, 5=Advanced): "))
    hours = int(input("Weekly study hours: "))
    deadline = int(input("Target deadline (months): "))

    return {
        "level": level,
        "hours": hours,
        "deadline": deadline
    }


def get_weights():

    print("\n--- Select Your Main Priority ---")
    print("1. Get Job Quickly")
    print("2. High Salary Focus")
    print("3. Easy Learning")
    print("4. Strong Foundation")
    print("5. Balanced")

    choice = int(input("Enter choice (1-5): "))

    if choice == 1:      # Fast job
        return {
            "demand": 5,
            "roi": 4,
            "time": 5,
            "difficulty": 3,
            "resources": 3
        }

    elif choice == 2:    # Salary
        return {
            "demand": 4,
            "roi": 5,
            "time": 3,
            "difficulty": 4,
            "resources": 3
        }

    elif choice == 3:    # Easy
        return {
            "demand": 3,
            "roi": 3,
            "time": 4,
            "difficulty": 5,
            "resources": 4
        }

    elif choice == 4:    # Foundation
        return {
            "demand": 4,
            "roi": 4,
            "time": 2,
            "difficulty": 5,
            "resources": 5
        }

    else:               # Balanced
        return {
            "demand": 4,
            "roi": 4,
            "time": 4,
            "difficulty": 4,
            "resources": 4
        }


def main():

    print("==== Learning Path Decision Companion ====\n")

    print("Select Mode:")
    print("1. Get Recommendation")
    print("2. Choose Path Manually")

    mode = int(input("Enter choice (1-2): "))

    paths = load_paths()

    # Manual Mode
    if mode == 2:

        print("\nAvailable Paths:\n")

        for i, p in enumerate(paths, 1):
            print(f"{i}. {p['name']}")

        choice = int(input("\nSelect a path: "))

        selected = paths[choice - 1]

        print("\nYou Selected:")
        print(selected["name"])
        print(selected["description"])

        return


    # Recommendation Mode
    profile = get_profile()
    weights = get_weights()

    ranked = rank_paths(paths, weights, profile)

    print("\n--- Recommended Paths ---\n")

    for i, p in enumerate(ranked, 1):

        print(f"{i}. {p['name']} (Score: {p['score']:.2f})")
        print(f"   {p['description']}")

        reasons = explain(p, profile)

        print("   Why:")
        for r in reasons:
            print(f"    - {r}")

        print()


if __name__ == "__main__":
    main()