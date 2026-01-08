def calculate_risk(results):
    risk_weights = {
        "low": 10,
        "medium": 25,
        "high": 50,
        "critical": 100
    }

    total_risk = 0
    breakdown = {
        "low": 0,
        "medium": 0,
        "high": 0,
        "critical": 0
    }

    for item in results:
        risk = item.get("risk")
        if risk in risk_weights:
            total_risk += risk_weights[risk]
            breakdown[risk] += 1

    score = max(0, 100 - total_risk)

   
    if score >= 80:
        grade = "Secure"
    elif score >= 50:
        grade = "Moderate Risk"
    else:
        grade = "High Risk"

    return {
        "security_score": score,
        "grade": grade,
        "risk_breakdown": breakdown,
        "total_findings": len(results)
    }