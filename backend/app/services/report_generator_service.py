def generate_report(
    organization_name,
    esg_score,
    carbon_emission,
    energy_usage
):
    return f"""
ESG REPORT

Organization: {organization_name}

ESG Score: {esg_score}
Carbon Emission: {carbon_emission} tons CO2
Energy Usage: {energy_usage} kWh

AI Summary:
The organization demonstrates sustainability performance
with an ESG score of {esg_score}. Further carbon reduction
and energy optimization initiatives are recommended.
"""