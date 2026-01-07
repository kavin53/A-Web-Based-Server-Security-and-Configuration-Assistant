def analyze_risk(results):
    score = 0
    issues = 0

    for item in results:
        risk = item.get("risk")

        if risk == "high":
            score += 30
            issues += 1
        elif risk == "medium":
            score += 15
            issues += 1
        elif risk == "low":
            score += 5

    if score >= 60:
        level = "HIGH"
        recommendation = "Immediate security hardening required"
    elif score >= 30:
        level = "MEDIUM"
        recommendation = "Security improvements recommended"
    else:
        level = "LOW"
        recommendation = "No critical security risks detected"

    return {
        "risk_score": score,
        "overall_risk": level,
        "issues_found": issues,
        "final_recommendation": recommendation
    }
