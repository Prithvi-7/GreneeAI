def generate_digital_twin(
    carbon_emission: float,
    energy_usage: float,
    water_consumption: float
):

    score = 100 - (
        (carbon_emission * 0.05) +
        (energy_usage * 0.01) +
        (water_consumption * 0.02)
    )

    score = max(0, round(score, 2))

    if score >= 80:
        status = "Excellent"
        recommendation = (
            "Organization is highly sustainable."
        )

    elif score >= 60:
        status = "Good"
        recommendation = (
            "Further optimization can improve sustainability."
        )

    else:
        status = "Needs Improvement"
        recommendation = (
            "Reduce emissions and resource consumption."
        )

    return {
        "sustainability_score": score,
        "status": status,
        "recommendation": recommendation
    }