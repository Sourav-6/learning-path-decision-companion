def calculate_score(path, weights, profile):

    # Normalize duration (shorter is better)
    time_score = max(0, 25 - path["duration_weeks"])

    difficulty_match = max(
        0,
        5 - abs(path["difficulty"] - profile["level"])
    )

    score = (
        path["job_demand"] * weights["demand"] +
        path["roi"] * weights["roi"] +
        time_score * weights["time"] +
        difficulty_match * weights["difficulty"] +
        path["resources"] * weights["resources"]
    )

    return score


def rank_paths(paths, weights, profile):

    for p in paths:
        p["score"] = calculate_score(p, weights, profile)

    paths.sort(key=lambda x: x["score"], reverse=True)

    return paths