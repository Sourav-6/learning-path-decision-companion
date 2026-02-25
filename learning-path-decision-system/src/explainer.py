def explain(path, profile):

    reasons = []

    if path["job_demand"] >= 4:
        reasons.append("High job market demand")

    if path["roi"] >= 4:
        reasons.append("Strong career return on investment")

    if path["difficulty"] <= profile["level"] + 1:
        reasons.append("Difficulty matches your current level")

    if path["resources"] >= 4:
        reasons.append("Good quality learning resources available")

    if path["duration_weeks"] <= profile["deadline"] * 4:
        reasons.append("Fits within your target timeline")

    return reasons