def forecast_energy_usage(last_6_months_usage):

    average_usage = sum(last_6_months_usage) / len(last_6_months_usage)

    if last_6_months_usage[-1] > last_6_months_usage[0]:
        trend = "Increasing"
        predicted_next_month = average_usage * 1.05
    else:
        trend = "Stable"
        predicted_next_month = average_usage

    return {
        "predicted_next_month": round(predicted_next_month, 2),
        "trend": trend
    }