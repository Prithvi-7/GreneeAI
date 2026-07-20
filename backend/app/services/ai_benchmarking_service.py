def benchmark_analysis(
    organization_score: float,
    industry_average: float
):

    gap = round(
        organization_score - industry_average,
        2
    )

    if gap > 0:
        ranking = "Above Average"
        recommendation = (
            "Maintain current sustainability practices "
            "and continue innovation."
        )

    elif gap < 0:
        ranking = "Below Average"
        recommendation = (
            "Improve ESG initiatives and reduce "
            "environmental impact."
        )

    else:
        ranking = "Industry Average"
        recommendation = (
            "Performance matches industry standards."
        )

    return {
        "ranking": ranking,
        "gap": gap,
        "recommendation": recommendation
    }