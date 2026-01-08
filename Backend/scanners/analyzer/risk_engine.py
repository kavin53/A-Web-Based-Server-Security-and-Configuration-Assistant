def calculate_risk(results):
    weights = {
        "low": 1,
        "medium": 4,
        "high": 7
    }

    total_score = 0
    breakdown = {
        "low": 0,
        "medium": 0,
        "high": 0
    }

    for item in results:
        risk = item.get("risk", "low").lower()
        score = weights.get(risk, 0)
        total_score += score

        if risk in breakdown:
            breakdown[risk] += 1

    # Determine overall risk level
    if total_score <= 5:
        overall = "LOW"
    elif total_score <= 15:
        overall = "MEDIUM"
    else:
        overall = "HIGH"

    return {
        "total_score": total_score,
        "overall_risk": overall,
        "breakdown": breakdown
    }
