def process_esg_query(query: str):

    query = query.lower()

    if "carbon" in query:
        return {
            "response": "Reduce emissions by improving energy efficiency and adopting renewable energy.",
            "action": "Carbon Reduction Plan"
        }

    elif "energy" in query:
        return {
            "response": "Monitor peak-hour usage and optimize HVAC systems.",
            "action": "Energy Optimization"
        }

    elif "compliance" in query:
        return {
            "response": "Review ESG reports and regulatory requirements regularly.",
            "action": "Compliance Review"
        }

    return {
        "response": "ESG Agent analyzed your request.",
        "action": "General Recommendation"
    }