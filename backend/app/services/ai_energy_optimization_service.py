def optimize_energy(monthly_units: float, monthly_cost: float):

    cost_per_unit = monthly_cost / monthly_units

    if cost_per_unit > 8:
        efficiency_score = 60
        recommendation = (
            "High energy cost detected. "
            "Switch to LED lighting, optimize HVAC systems, "
            "and monitor peak-hour consumption."
        )
        estimated_savings = monthly_cost * 0.15

    else:
        efficiency_score = 85
        recommendation = (
            "Energy consumption is reasonably optimized. "
            "Continue monitoring usage and adopt renewable energy."
        )
        estimated_savings = monthly_cost * 0.05

    return {
        "efficiency_score": efficiency_score,
        "recommendation": recommendation,
        "estimated_savings": round(estimated_savings, 2)
    }