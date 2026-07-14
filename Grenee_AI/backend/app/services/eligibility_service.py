def check_eligibility(data):
    category = data.get("category")
    state = data.get("state")
    organization_type = data.get("organization_type")
    employee_count = data.get("employee_count")

    if (
        category == "Solar"
        and state == "Tamil Nadu"
        and organization_type == "MSME"
        and employee_count >= 10
    ):
        return {
            "eligible": True,
            "message": "Eligible for Solar Rooftop Subsidy",
            "estimated_amount": 200000
        }

    if (
        category == "EV"
        and organization_type == "Manufacturing"
    ):
        return {
            "eligible": True,
            "message": "Eligible for EV Promotion Scheme",
            "estimated_amount": 150000
        }

    return {
        "eligible": False,
        "message": "Currently not eligible for the selected subsidy.",
        "estimated_amount": 0
    }