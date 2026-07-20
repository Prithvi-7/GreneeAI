def predict_compliance(esg_score: float, compliance_rate: float):

    if esg_score >= 80 and compliance_rate >= 80:
        return {
            "risk_level": "Low Risk",
            "recommendation": "Organization is compliant and performing well."
        }

    elif esg_score >= 60 and compliance_rate >= 60:
        return {
            "risk_level": "Medium Risk",
            "recommendation": "Improve ESG practices and compliance monitoring."
        }

    else:
        return {
            "risk_level": "High Risk",
            "recommendation": "Immediate corrective actions are required."
        }