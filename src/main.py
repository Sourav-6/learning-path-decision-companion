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

    print("\n--- Set Priorities (1=Low, 5=High) ---")

    return {
        "demand": int(input("Job Demand: ")),
        "roi": int(input("Career ROI: ")),
        "time": int(input("Fast Completion: ")),
        "difficulty": int(input("Difficulty Match: ")),
        "resources": int(input("Learning Resources: "))
    }


def main():

    print("==== Learning Path Decision Companion ====")

    profile = get_profile()
    weights = get_weights()

    paths = load_paths()

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